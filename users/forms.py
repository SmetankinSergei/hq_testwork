from django import forms
from django.contrib.auth import get_user_model


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Repeat password')

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'password2']

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Password mismatch')
        return data['password']
