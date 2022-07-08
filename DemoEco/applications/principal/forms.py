from django import forms
from django.contrib.auth import authenticate

from .models import User


class RegisterForm(forms.ModelForm):
    
    password1 = forms.CharField(
            label='Contraseña',
            required=True,
            widget=forms.PasswordInput()
        )
    
    password2 = forms.CharField(
            label='Repetir contraseña',
            required=True,
            widget=forms.PasswordInput()
        )
        
    class Meta:
        model=User 
        fields=('username','email','nombres','apellidos')
        
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            #self.add_error('password2', 'Contraseñas no coincidentes')#ERROR EN LA VALIDACION DEL FORMULARIO
            raise forms.ValidationError('Contraseñas no coincidentes')
            
    
class LoginForm(forms.Form):
    
    username = forms.CharField(
        label='Username',
        required=True
    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(),
        
    )

    def clean(self):  
        username=self.cleaned_data['username'] 
        password=self.cleaned_data['password']

        if not authenticate(username=username,password=password):
            raise forms.ValidationError('Datos de usuario incorrectos')
    