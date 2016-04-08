from django.conf.urls import url

from .views import SubscribeView

urlpatterns = [
    url(r'^subscribe', SubscribeView.as_view(), name='subscribe'),
    ]
