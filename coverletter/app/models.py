# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PersonInfo(models.Model):
    PersonName = models.CharField(max_length=255)
    CompanyName = models.CharField(max_length=255)