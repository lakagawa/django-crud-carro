# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Carro(models.Model):
    modelo = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    ano = models.CharField(max_length=4)

    created_date = models.DateTimeField(
            auto_now_add=True)

    def __str__(self):
        return self.modelo
