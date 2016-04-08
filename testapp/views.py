from django.shortcuts import render

from .forms import SubscribeForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView

class SubscribeView(FormView):
    template_name = 'testapp/subscribe.html'
    form_class = SubscribeForm
    success_url = reverse_lazy('form_data_valid')
