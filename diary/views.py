# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime as dt
from .models import Images

# Create your views here.
def welcome(request):
    new = Images.get_image()
    return render (request, 'index.html', {"new":new})

def search_results(request):
    
    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images_by_category = Images.search_by_category(search_term)
        searched_images_by_location = Images.search_by_location(search_term)
        results = [*searched_images_by_category, *searched_images_by_location]
        message = f"{search_term}"
        
        return render (request, 'search.html', {"message":message, "results":results})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})