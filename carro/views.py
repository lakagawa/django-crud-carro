# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import ModelForm
from django.shortcuts import render, redirect

# Create your views here.
from .models import *


class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields = ['modelo', 'marca', 'ano']


def cadastrar_carro(request, template_name='carro_form.html'):
    form = CarroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('carro_list')
    return render(request, template_name, {'form': form})


def listar_carro(request, template_name="carro_list.html"):
    carro = Carro.objects.all()
    return render(request, template_name, {'lista': carro})
