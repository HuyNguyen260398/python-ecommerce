from django.conf.urls import url

from .views import SearchProducView

urlpatterns = [
    url(r'^$', SearchProducView.as_view(), name='query'),
]
