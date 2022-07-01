from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

#HERENCIA DE USUARIOS DE DJANGO
class User(AbstractBaseUser, PermissionsMixin):
    
    username=models.CharField(max_length=20, unique=True) #nombre de usuario
    nombres=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    email=models.EmailField()
    
    is_active=models.BooleanField(default=False)#Indica si el usuario esta activo. Facilita la desactivación desde el admin
    is_staff=models.BooleanField(default=False) #Especifica si puede o no entrar al admin. Por defecto no
    
    USERNAME_FIELD = 'username' 
    REQUIRED_FIELDS=['email',] #Campos requeridos para el admin 

    objects=UserManager()
    
    

    
