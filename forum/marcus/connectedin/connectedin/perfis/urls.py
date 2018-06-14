# connectedin/perfis/urls.py 
from django.conf.urls import url
from perfis.views import index, exibir

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^perfis$', exibir, name='exibir'),
]