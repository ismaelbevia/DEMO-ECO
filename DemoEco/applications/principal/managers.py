"""
Aqui manejaremos los usuarios
"""

from django.db import models

from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):      
    #Crear cualquier usuario ESTA ES LA BASE DE TODO
    def _create_user(self, username, email, password, is_staff, is_superuser,is_active, **extra_fields):
        
        user=self.model(
            username=username,
            email=email,
            is_staff=is_staff, 
            is_superuser=is_superuser, #SUPER USER
            is_active=is_active,
            **extra_fields
            )
        
        user.set_password(password) #La encriptamos 
        user.save(using=self.db) #utilizamos la base de datos predeterminada del admin por lo que es necesario utilizar estos parametros en el save. si se desea usar la base de datos predeterminada, use user.save(using=self._db)
        return user
        
    #USUARIO DEL ADMIN
    def create_superuser(self,username,email,password=None,**extra_fields):
        return self._create_user(username,email,password,True,True,True,**extra_fields)

    #USUARIO NORMAL
    def create_user(self, username, email, password=None,**extra_fields):
        return self._create_user(username,email, password,False,False,True,**extra_fields)
    
    #None es el valor predeterminado para que hace que no se proporciona explícitamente. 