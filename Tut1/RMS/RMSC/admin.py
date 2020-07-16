# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import User,Operations,Resource,ResourceAccess


#admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('fname','lname','username')
admin.site.register(User, UserAdmin)

#admin.site.register(Operations)
@admin.register(Operations)
class OperationsAdmin(admin.ModelAdmin):
    pass

#admin.site.register()
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display=('rname','r_description','creation_date','owner_id')

#admin.site.register()
@admin.register(ResourceAccess)
class ResourceAccessAdmin(admin.ModelAdmin):
    pass