# -*- coding: utf- -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import User,Resource,ResourceAccess

# Create your views here.
def index(request):
	users = User.objects.all()
	res = Resource.objects.all()
	access = ResourceAccess.objects.all()
	return render(request,'RMSC/index.html', {'users':users,'res':res})
