from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from .models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html
    )
    repeat_password = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data["password"]

        if password:
            password_validation.validate_password(password)

        return password

    def clean(self):
        super().clean()

        password = self.cleaned_data['password']
        repeat_password = self.cleaned_data['repeat_password']

        if password and repeat_password and password != repeat_password:
            errors = {
                'repeat_password': ValidationError(
                    'The passwords entered do not match',
                    code='password_mismatch'
                )
            }
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        user.is_activated = True
        user.slug = slugify(self.cleaned_data['username'])

        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'repeat_password',
            'email',
            'age',
            'image',
            'gender',
            'country'
        ]
