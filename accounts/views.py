import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import *
from django.utils.encoding import force_text
from django.contrib.auth import login as auth_login

from .forms import MyUserCreationForm, MyAuthenticationForm
from .models import MyUser

class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = MyUserCreationForm
    success_url = reverse_lazy('form_data_valid')

    def post(self, request, **kwargs):
        print "Received post request"
        if request.is_ajax():
            return self.ajax(request)
        return super(RegisterView, self).post(request, **kwargs)

    def ajax(self, request):
        print "Received ajax request"
        form = self.form_class(data=json.loads(request.body))
        response_data = {'errors': form.errors, 'success_url': force_text(self.success_url)}
        return HttpResponse(json.dumps(response_data), content_type="application/json")

class AuthView(FormView):
    template_name = 'accounts/login.html'
    form_class = MyAuthenticationForm
    success_url = reverse_lazy('home')
    
    def post(self, request, **kwargs):
        print "Received post request"
        if request.is_ajax():
            return self.ajax(request)
        return super(RegisterView, self).post(request, **kwargs)

    def ajax(self, request):
        print "Received ajax request"
        form = self.form_class(data=json.loads(request.body))
        if form.is_valid():
            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())
            
        response_data = {'errors': form.errors, 'success_url': force_text(self.success_url)}
        return HttpResponse(json.dumps(response_data), content_type="application/json")


class UserDetail(DetailView):
    template_name = 'accounts/user_detail.html'
    model = MyUser
    context_object_name = 'user'

class UserList(ListView):
    template_name = 'accounts/user_list.html'
    context_object_name = 'users'
    model = MyUser
