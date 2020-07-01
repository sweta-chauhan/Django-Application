# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import User,Operations,Resource,Resource_Access

admin.site.register(User)
admin.site.register(Operations)
admin.site.register(Resource)
admin.site.register(Resource_Access)
