from django.conf.urls import url
from . import views


urlpatterns = [
    #url(r'^$', views.lista_parqueos, name ='lista_parqueos'),
    url(r'^$', views.parqueo_nuevo, name='parqueo_nuevo'),
    ]
