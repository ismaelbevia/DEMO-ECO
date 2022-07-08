from django import forms

from .models import MensajesSolicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = MensajesSolicitud
        fields=('__all__')