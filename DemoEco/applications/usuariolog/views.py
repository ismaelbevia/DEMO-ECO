from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ListaView(LoginRequiredMixin,TemplateView):
    template_name = 'usuariolog/lista.html'
    login_url=reverse_lazy('principal_app:login')