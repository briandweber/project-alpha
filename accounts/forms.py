from django import forms
from django.contrib.auth.models import User
from accounts.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(
        max_length=150, widget=forms.PasswordInput
    )


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput()
    )
    email = forms.EmailField(
        required=True, widget=forms.TextInput()
    )
    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "avatar",
            "bio",
            "first_name",
            "last_name",
            "email",
        ]
