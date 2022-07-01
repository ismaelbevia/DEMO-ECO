
from django.contrib import admin
from django.urls import path

from . import views

app_name="usuariolog_app"

urlpatterns = [
    path('lista/',views.ListaView.as_view(),name="lista"),
]