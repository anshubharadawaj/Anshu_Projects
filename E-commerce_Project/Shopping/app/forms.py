from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.utils.translation import gettext as _


class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput()),
    password2 = forms.CharField(label='Confirm Password',
                        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput())

    def __init__(self, *args, **kwargs):
        super(CustomerRegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widget = {'username': forms.TextInput()}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True})),
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class MyChangePasswordForm(PasswordChangeForm):
    old_password =forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True}),
    )

    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("Confirm New password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )


    def __init__(self, *args,**kwargs):
        super(MyChangePasswordForm, self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class']='form-control'

