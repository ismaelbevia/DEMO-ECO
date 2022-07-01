
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, FormView

from .models import User 
from .forms import RegisterForm, LoginForm
from django.urls import reverse_lazy, reverse

# Create your views here.

class InicioView(TemplateView):
    template_name = 'index.html'
    
class UserRegisterView(FormView):
    template_name='principal/register.html'
    form_class= RegisterForm
    success_url=reverse_lazy('principal_app:inicio')
    
    
    def form_valid(self, form):
        usuario=User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            )
        messages.success(self.request, "Registro exitoso")
        return HttpResponseRedirect(reverse('principal_app:login'))
    
    
class LoginUserView(FormView):
    template_name='principal/login.html'
    form_class=LoginForm
    success_url=reverse_lazy('usuariolog_app:lista')
    
    def form_valid(self, form):
        
        user=authenticate( #VERIFICADO en la view y creamos user
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
            )
        
        login(self.request, user)
        return super(LoginUserView,self).form_valid(form)
        
    
