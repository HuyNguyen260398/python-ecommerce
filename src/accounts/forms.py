from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class GuestForm(forms.Form):
    email = forms.EmailField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        label='Comfirm Password',
        widget=forms.PasswordInput
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)

        if qs.exists():
            raise forms.ValidationError('Username already exist!')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not ("@gmail.com" in email):
            raise forms.ValidationError('Email has to be abc@gmail.com')

        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email already taken!')
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Password does not match!')

        return data
