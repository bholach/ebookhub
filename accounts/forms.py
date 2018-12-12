from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignInForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username', 'password1')


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
