from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

# Create your models here.

class Usuario(AbstractBaseUser, PermissionsMixin):


    
    
    username = models.CharField('Nombre de Usuario',max_length=10, unique=True)
    email = models.EmailField('Correo Electrónico',max_length=254, unique=True)
    
    
    #
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username' 
    REQUIRED_FIELDS = ['email',] 

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    objects = UserManager() # Para crear los usuarios es necesario los managers por ello lo creamos

    # Estas dos funciones trabajan de la misma manera como lo haríamos con __srt__
       
    def get_short_name(self):
        return self.username
    
   

