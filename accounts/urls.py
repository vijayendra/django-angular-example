from django.conf.urls import url, include

from accounts import views as accounts_views

urlpatterns = [
    url(r'^login/', accounts_views.login, name='login')
]
