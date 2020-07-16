# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
    def save(self, *args, **kwargs):
        if self.name == "" :
            return # Yoko shall never have her own blog!
        else:
            super().save(*args, **kwargs)

class Resource(models.Model):
    rname = models.CharField(max_length=20)
    r_description = models.CharField(max_length=50)
    creation_date = models.DateTimeField('date published')
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.rname

    def save(self, *args, **kwargs):
        '''
        Overidding save function to perform insert into query in database.
        '''
        if self.name == "" :
            return # Yoko shall never have her own blog!
        else:
            super().save(*args, **kwargs)

class Operations(models.Model):
    opt_name = models.CharField(max_length=6,unique=True)
    
    def __str__(self):
        return self.opt_name

    def save(self, *args, **kwargs):
        '''
        Overidding save function to perform insert into query in database.
        '''
        if self.name == "" :
            return
        else:
            super().save(*args, **kwargs)

    
class ResourceAccess(models.Model):
    rid = models.ForeignKey(Resource, on_delete=models.CASCADE)
    oid = models.ForeignKey(Operations, on_delete=models.CASCADE)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)

