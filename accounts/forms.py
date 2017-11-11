from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class SignUpForm(forms.ModelForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )

    class Meta:
        model = User
        fields = ('first_name', 'email')

    def clean_password(self):
        password = self.cleaned_data.get("password")
        password_validation.validate_password(password, self.instance)
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
