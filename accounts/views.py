import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import *
from django.utils.encoding import force_text

from .forms import MyUserCreationForm
from .models import MyUser

class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = MyUserCreationForm
    success_url = reverse_lazy('form_data_valid')

class UserDetail(DetailView):
    template_name = 'accounts/user_detail.html'
    model = MyUser
    context_object_name = 'user'

class UserList(ListView):
    template_name = 'accounts/user_list.html'
    context_object_name = 'users'
    model = MyUser
