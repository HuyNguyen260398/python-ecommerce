from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from django.db import models
from django.db.models.signals import pre_save, post_save

from .signals import object_viewed_signal
from .utils import get_client_ip

from accounts.signals import user_logged_in_signal


User = settings.AUTH_USER_MODEL


FORCE_SESSION_TO_ONE = getattr(settings, 'FORCE_SESSION_TO_ONE', False)
FORCE_INACTIVE_USER_END_SESSION = getattr(settings, 'FORCE_INACTIVE_USER_END_SESSION', False)


class ObjectViewed(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    ip_address = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} viewed on {}".format(self.content_object, self.timestamp)

    class Meta:
        ordering = ['-timestamp']  # most recent saved show up first
        verbose_name = 'Object viewed'
        verbose_name_plural = 'Objects viewed'


class UserSession(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    ip_address = models.CharField(max_length=255, blank=True, null=True)
    session_key = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    ended = models.BooleanField(default=False)

    def end_session(self):
        session_key = self.session_key
        ended = self.ended
        try:
            Session.objects.get(pk=session_key).delete()
            self.active = False
            self.ended = True
            self.save()
        except:
            pass
        return self.ended


def object_viewed_receiver(sender, instance, request, *args, **kwargs):
    c_type = ContentType.objects.get_for_model(sender)  # equal to instance.__class__
    authenticated_user = None
    if request.user.is_authenticated():
        authenticated_user = request.user
    new_view_obj = ObjectViewed.objects.create(
        user=authenticated_user,
        ip_address=get_client_ip(request),
        content_type=c_type,
        object_id=instance.id
    )


object_viewed_signal.connect(object_viewed_receiver)


def user_logged_in_receiver(sender, instance, request, *args, **kwargs):
    user = instance
    ip_address = get_client_ip(request)
    session_key = request.session.session_key
    UserSession.objects.create(
        user=user,
        ip_address=ip_address,
        session_key=session_key
    )


user_logged_in_signal.connect(user_logged_in_receiver)


def post_save_session_receiver(sender, instance, created, *args, **kwargs):
    if created:
        qs = UserSession.objects.filter(user=instance.user, ended=False,
                                        active=False).exclude(id=instance.id)
        for i in qs:
            i.end_session()
    if not instance.active and not instance.ended:
        instance.end_session()


if FORCE_SESSION_TO_ONE:
    post_save.connect(post_save_session_receiver, sender=UserSession)


def post_save_user_changed_receiver(sender, instance, created, *args, **kwargs):
    if not created:
        if instance.is_active == False:
            qs = UserSession.objects.filter(user=instance.user, ended=False, active=False)
            for i in qs:
                i.end_session()


if FORCE_INACTIVE_USER_END_SESSION:
    post_save.connect(post_save_user_changed_receiver, sender=User)
