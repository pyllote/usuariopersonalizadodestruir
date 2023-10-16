from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from django.forms import fields
from django import forms
from django.forms.widgets import PasswordInput

from django.views.generic.edit import FormView # necesario para el formulario de regisro personalizado

from .models import Usuario



class UsuarioCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UsuarioCreationForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Usuario
        fields = ('username',)



class UsuarioChangeForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super(UsuarioChangeForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Usuario
        fields = '__all__'




class Userform(forms.ModelForm):

    password = forms.CharField(widget=PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        ))

    class Meta:

        model = Usuario
        fields = ['username','email','password']
        widget = {'email':forms.EmailInput,'password':forms.PasswordInput}
    
   

    def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({'class':'form-control'})







#---Formulario para registro de usuario (SANTA CRUZ)

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña'
            }
        )
    )

    class Meta:
        """Meta definition for Userform."""

        model = Usuario
        fields = (
            'username',
            'email',
            
            
        )

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({'class':'form-control'})
    

    def clean_password2(self):

        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')


#--Formulario para actualizar password (SANTA CRUZ)

class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )