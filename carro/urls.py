from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^cadastrar_carro/', cadastrar_carro, name='cadastrar_carro'),
    url(r'^listar_carros/', listar_carro, name='carro_list'),
]
