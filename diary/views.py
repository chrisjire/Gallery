# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return render (request, 'index.html')

