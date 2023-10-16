from django.contrib.auth.models import BaseUserManager

from django.db import models


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username,email, password, is_staff, is_superuser,is_active, **extra_fields):

        

        if not email:
            raise ValueError('Debe especificar email')
        
        email = self.normalize_email(email)

        
        user = self.model(
           username=username,
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user( username, email, password, False, False,True, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True, True,True, **extra_fields) 