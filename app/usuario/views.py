from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from django.views.generic.edit import FormView #--Necesario para registrar nuevo usuario
from django.contrib.auth import authenticate, login, logout #--Necesario para cambiar contraseña

from .models import Usuario
from .forms import UserRegisterForm, UpdatePasswordForm
# Create your views here.


class UserRegisterView(FormView):

    template_name = 'usuario/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        
        usuario = Usuario.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
              
        )

        return super(UserRegisterView, self).form_valid(form)



class UpdatePasswordView(FormView):
    template_name = 'usuario/update.html'
    form_class = UpdatePasswordForm
    #success_url = '/'
    success_url = reverse_lazy('base:login')
    #login_url = reverse_lazy('base:login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username=usuario.username,
            password=form.cleaned_data['password1']
        )
        
        if user:
           
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()
            print("AUTENTICADO")

        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)