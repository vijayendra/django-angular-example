from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from .forms import MyAuthenticationForm
from .views import RegisterView, UserList, UserDetail

app_name = 'user'

urlpatterns = [
    url(r'^$', UserList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', UserDetail.as_view(), name='detail'),
    url(r'^login/$', auth_views.login, {'authentication_form': MyAuthenticationForm}, name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
]
