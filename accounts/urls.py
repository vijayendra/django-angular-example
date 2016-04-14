from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from .forms import MyAuthenticationForm
from .views import RegisterView, UserList, UserDetail, AuthView

app_name = 'user'

urlpatterns = [
    url(r'^$', UserList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', UserDetail.as_view(), name='detail'),
    url(r'^login/$', AuthView.as_view(), name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'accounts/logged_out.html'}, name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
]
