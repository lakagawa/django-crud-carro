from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^cadastrar_usuario', cadastrar_usuario, name='cadastrar_usuario'),
    url(r'^login', do_login, name='login'),
    url(r'^logout', do_logout, name='logout'),
    url(r'^cadastrar_carro', cadastrar_carro, name='cadastrar_carro'),
    url(r'^listar_carros', listar_carro, name='carro_list'),
    url(r'^editar_carro/(?P<pk>[0-9]+)', editar_carro, name='editar_carro'),
    url(r'^remover_carro/(?P<pk>[0-9]+)', remover_carro, name='remover_carro'),
]
