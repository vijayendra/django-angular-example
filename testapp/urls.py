from django.conf.urls import url
from django.views.generic import TemplateView

from .views import SubscribeView, ModelScopeSubscribeView

urlpatterns = [
    url(r'^subscribe/$', SubscribeView.as_view(), name='subscribe'),
    url(r'^subscribe-model-scope/$', ModelScopeSubscribeView.as_view(), name='model-scope'),
    url(r'^form_data_valid/$', TemplateView.as_view(template_name="testapp/form-data-valid.html"), name='form_data_valid'),
    
    ]
