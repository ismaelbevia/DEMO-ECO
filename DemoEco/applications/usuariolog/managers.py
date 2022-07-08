from django.db import models

class EcosManager(models.Manager):
    def ecos_publicas(self):
        return self.filter(
            publico=True,
            ).order_by('-fecha')
    def ecos_usuario(self, user):
        return self.filter(
            usuario=user,
            ).order_by('-fecha')