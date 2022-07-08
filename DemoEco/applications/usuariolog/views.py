import csv
import html 

from django.utils.encoding import smart_str#Para escribir el csv
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from .models import Ecos

# Create your views here.

class ListaView(LoginRequiredMixin,ListView):
    template_name = 'usuariolog/lista.html'
    login_url=reverse_lazy('principal_app:login')
    context_object_name='ecos'
    paginate_by=10
    
    def get_queryset(self):     
        resultado=Ecos.objects.ecos_publicas()
        print(resultado)
        return resultado
    
    
class ListaUsuarioView(LoginRequiredMixin,ListView):
    template_name = 'usuariolog/perfil.html'
    login_url=reverse_lazy('principal_app:login')
    context_object_name='ecos'
    paginate_by=8
    
    def get_queryset(self):     
        resultado=Ecos.objects.ecos_usuario(self.request.user)
        return resultado
    
    
class EcoView(LoginRequiredMixin,DetailView):
    template_name="usuariolog/vista.html"
    login_url=reverse_lazy('principal_app:login')
    model=Ecos
    context_object_name='eco'
    
    
class EcoUpdateView(LoginRequiredMixin,UpdateView):
    model=Ecos
    template_name='usuariolog/update.html'
    #form_class=
    fields=['paciente','idP','descripcion_corta','descripcion','archivo','publico']
    success_url=reverse_lazy('usuariolog_app:perfil')
    login_url=reverse_lazy('principal_app:login')

    
class EcoDeleteView(LoginRequiredMixin,DeleteView):
    template_name='usuariolog/delete.html'
    model=Ecos
    success_url=reverse_lazy('usuariolog_app:perfil')
    login_url=reverse_lazy('principal_app:login')

class DescargarListaView(LoginRequiredMixin,View):
    login_url=reverse_lazy('principal_app:login')
    
    def get(self, request, *args, **kwargs):

        kword=self.kwargs['pk']
        print (kword)

        # Tipo del contenido
        response = HttpResponse(content_type='text/csv')
        #Nombre del csv
        response['Content-Disposition'] = 'attachment; filename="ListaEcos.csv"'
        writer = csv.writer(response)
        #headers
        writer.writerow([
         smart_str("fecha"),
         smart_str("usuario"),
         smart_str("paciente"),
         smart_str("idPaciente"),
         smart_str("descripcion corta"),
         smart_str("archivo"),
        ])

        if kword=='1':
            datos = Ecos.objects.ecos_publicas()
        else:
            datos = Ecos.objects.ecos_usuario(self.request.user)
        
        for datos in datos:
            writer.writerow([
             smart_str(datos.fecha),
             smart_str(datos.usuario),
             smart_str(datos.paciente),
             smart_str(datos.idP),
             smart_str(datos.descripcion_corta),
             smart_str(datos.archivo),
              ])
        
        return response
    
    
# =============================================================================
# class DescargarView(LoginRequiredMixin,View):
#     login_url=reverse_lazy('principal_app:login')
#     
#     def get(self, request, *args, **kwargs):
#         datos = Ecos.objects.get(id=self.kwargs['pk'])
#         
#         # Tipo del contenido
#         response = HttpResponse(content_type='text/csv')
#      
#         #Nombre del csv
#         response['Content-Disposition'] = 'attachment; filename="'+datos.paciente+'-'+datos.descripcion_corta+'.csv"'
#      
#         writer = csv.writer(response)
#      
#         #headers
#         writer.writerow([
#          smart_str("fecha"),
#          smart_str("usuario"),
#          smart_str("paciente"),
#          smart_str("idPaciente"),
#          smart_str("descripcion corta"),
#          smart_str("descripcion"),
#          smart_str("archivo"),
#          smart_str("publico"),
#         ])
#         
#         writer.writerow([
#          smart_str(datos.fecha),
#          smart_str(datos.usuario),
#          smart_str(datos.paciente),
#          smart_str(datos.idP),
#          smart_str(datos.descripcion_corta),
#          smart_str(datos.descripcion),
#          smart_str(datos.archivo),
#          smart_str(datos.publico),
#           ])
#         
#         return response
# =============================================================================
    
    