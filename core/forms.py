
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.urls import reverse

from .models import CustomUsuario


class CustomUsuarioCreationForm(UserCreationForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone', 'nasc')
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["username"]
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class CustomUsuarioChangeForm(UserChangeForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone')

class LoginForm(forms.ModelForm):

    class Meta:
        model = CustomUsuario
        fields = ('email', 'password')
        
    def login(self):
        user = CustomUsuario()
        user.email = self.cleaned_data['username']
        password = user.check_password(self.cleaned_data['password'])
        
        if user.email and password:
            return reverse('core:index')
    
