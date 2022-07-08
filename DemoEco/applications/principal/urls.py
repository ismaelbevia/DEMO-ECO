
from django.contrib import admin
from django.urls import path

from . import views

app_name="principal_app"

urlpatterns = [
    path('',views.InicioView.as_view(),name="inicio"),
    path('user_registro/',views.UserRegisterView.as_view(),name="user-registro"),
    path('login/',views.LoginUserView.as_view(),name="login"),
    path('logout/', views.LogoutView.as_view(),name='user-logout'),
]