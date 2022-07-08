
from django.contrib import admin
from django.urls import path

from . import views

app_name="usuariolog_app"

urlpatterns = [
    path('lista/',views.ListaView.as_view(),name="lista"),
    path('lista_usuario/',views.ListaUsuarioView.as_view(),name="perfil"),
    path('update_ecos/<pk>/',views.EcoUpdateView.as_view(),name="update"),
    path('delete_ecos/<pk>/',views.EcoDeleteView.as_view(),name="delete"),
    path('vista/<pk>/',views.EcoView.as_view(),name='vista'), 
    #path('descargar/<pk>/',views.DescargarView.as_view(),name='descargar'),
    path('descargarLista/<pk>/',views.DescargarListaView.as_view(),name='descargar-lista'),
]
