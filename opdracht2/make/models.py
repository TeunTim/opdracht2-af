from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse

# Create your models here.


class Tosti(models.Model):
    name = models.CharField(max_length=100, default ="")
    bread = models.IntegerField(default=0)
    cheese = models.IntegerField(default=0)
    ham = models.IntegerField(default=0)
    tomato = models.IntegerField(default=0)
    bacon = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    def __str__(self):
        return self.name

