# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.forms import ModelForm, PasswordInput
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.contrib.auth.models import User
from .models import *


def index(request, template_name='index.html'):
    return render(request, template_name)


class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields = ['modelo', 'marca', 'ano']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        password = PasswordInput()
        widgets = {'password': PasswordInput()}


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        password = PasswordInput()
        widgets = {'password': PasswordInput()}


def cadastrar_usuario(request, template_name='user_form.html'):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = User(username=form['username'].value(), email=form['email'].value())
        user.set_password(form['password'].value())
        user.save()
        return redirect('index')
    return render(request, template_name, {'form': form})


def do_login(request, template_name='login.html'):
    form = LoginForm(request.POST or None)
    user = authenticate(username=form['username'].value(), password=form['password'].value())
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('index')
        else:
            pass
            # Retorna uma mensagem de erro de 'conta desabilitada' .
    else:
        pass
        # Retorna uma mensagem de erro 'login inválido'.
    return render(request, template_name, {'form': form})


def do_logout(request):
    logout(request)
    return redirect('index')


def cadastrar_carro(request, template_name='carro_form.html'):
    form = CarroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('carro_list')
    return render(request, template_name, {'form': form})


def listar_carro(request, template_name="carro_list.html"):
    carro = Carro.objects.all()
    is_authenticated = request.user.is_authenticated()
    print(request.user.is_authenticated())

    return render(request, template_name, {'lista': carro, 'is_authenticated': is_authenticated})


def editar_carro(request, pk, template_name='carro_form.html'):
    carro = get_object_or_404(Carro, pk=pk)
    if not request.user.is_authenticated():
        return redirect('login')
    if request.method == "POST":
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('carro_list')
    else:
        form = CarroForm(instance=carro)
    return render(request, template_name, {'form': form})


def remover_carro(request, pk, template_name='carro_delete.html'):
    carro = Carro.objects.get(pk=pk)
    if not request.user.is_authenticated():
        return redirect('login')
    if request.method == "POST":
        carro.delete()
        return redirect('carro_list')
    return render(request, template_name, {'carro': carro})
