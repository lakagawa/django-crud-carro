# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Carro(models.Model):
    modelo = models.CharField(max_length=200, null=False)
    marca = models.CharField(max_length=200, null=False)
    ano = models.PositiveIntegerField(validators=[MinValueValidator(1900)], null=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.modelo
