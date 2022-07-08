from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import SolicitudForm

class SolicitudView(CreateView):
    template_name = 'solicitud/solicitudApp.html'
    form_class= SolicitudForm
    success_url=reverse_lazy('solicitud_app:solicitud-correcta')
    
class SCorrectaView(TemplateView):
    template_name = 'solicitud/scorrecta.html'
