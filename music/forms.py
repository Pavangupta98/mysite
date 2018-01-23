from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class Registration_form(UserCreationForm):

    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name',  'password', 'email']

    def save(self, commit=True):
        user = super(Registration_form, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user