
from django.contrib import admin
from django.urls import path

from . import views

app_name="solicitud_app"

urlpatterns = [
    path('solicitud/',views.SolicitudView.as_view(),name="solicitud"),
    path('solicitud-correcta/',views.SCorrectaView.as_view(),name="solicitud-correcta"),
]
