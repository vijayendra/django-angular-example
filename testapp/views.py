import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.utils.encoding import force_text

from .forms import SubscribeForm, ModelScopeSubscribeForm

class SubscribeView(FormView):
    template_name = 'testapp/subscribe.html'
    form_class = SubscribeForm
    success_url = reverse_lazy('form_data_valid')

class ModelScopeSubscribeView(FormView):
    template_name = 'testapp/model-scope.html'
    form_class = ModelScopeSubscribeForm
    success_url = reverse_lazy('form_data_valid')

    def post(self, request, **kwargs):
        print "Received post request"
        if request.is_ajax():
            return self.ajax(request)
        return super(ModelScopeSubscribeView, self).post(request, **kwargs)

    def ajax(self, request):
        print "Received ajax request"
        form = self.form_class(data=json.loads(request.body))
        response_data = {'errors': form.errors, 'success_url': force_text(self.success_url)}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
          
    
