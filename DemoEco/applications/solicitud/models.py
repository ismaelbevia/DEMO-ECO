from django.db import models

class MensajesSolicitud(models.Model):
    full_name=models.CharField('Nombre Completo', max_length=120)   
    movil=models.PositiveIntegerField('Telefono')
    email=models.EmailField('Email')
    empresa=models.CharField('Organización',blank=True, max_length=100)
    cuerpo=models.TextField('Mensaje')
    
    class Meta:
        verbose_name='Solicitud de Aplicación'
        verbose_name_plural ='Solicitudes de Aplicaciones'
    
    def __str__(self):
        return str(self.id) + '-' + self.full_name 