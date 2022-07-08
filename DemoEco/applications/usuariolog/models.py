from django.db import models

from applications.principal.models import User
from .managers import EcosManager

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Ecos(models.Model):
    fecha=models.DateTimeField(auto_now=True,editable=False)
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    paciente=models.CharField('Paciente',max_length=50)
    idP=models.CharField('Id del paciente',max_length=50)
    descripcion_corta=models.CharField('Descripción corta',max_length=100)
    descripcion=models.TextField('Descripion',blank=True)
    archivo=models.ImageField(upload_to='Ecos')
    publico=models.BooleanField('Publico')
    
    objects=EcosManager()
    
    class Meta:
        verbose_name='Recursos'
        verbose_name_plural ='Ecos'
        ordering =['id'] #ordenar por num
        
    def __str__(self):
        return str(self.id) + '-' + self.usuario.username + '-' + self.paciente