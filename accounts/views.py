from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import views as auth_views

from .forms import AuthenticationForm

def login(request):
    template_name = "accounts/login.html"
    return auth_views.login(request, template_name, AuthenticationForm)
    
