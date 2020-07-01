# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
	
class Resource(models.Model):
    rname = models.CharField(max_length=20)
    r_description = models.CharField(max_length=50)
    creation_date = models.DateTimeField('date published')
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Operations(models.Model):
    opt_name = models.CharField(max_length=6)
    

class Resource_Access(models.Model):
    rid = models.ForeignKey(Resource, on_delete=models.CASCADE)
    oid = models.ForeignKey(Operations, on_delete=models.CASCADE)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
