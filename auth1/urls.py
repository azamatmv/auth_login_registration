from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'login$', views.login),
    url(r'logget$', views.logget),
    url(r'auth$', views.auth_view),
    url(r'invalid$', views.invalid),
    url(r'logout$', views.logout),
    url(r'register$', views.register_user),
    url(r'register_success$', views.register_success),
]
