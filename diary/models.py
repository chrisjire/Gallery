# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name
    
    def save_editor(self):
        self.save()
    
    class Meta:
        ordering = ['first_name']

class tags(models.Model):
    name = models.CharField(max_length= 20)
    
    def __str__(self):
        return self.name

class Images(models.Model):
    image = models.ImageField(upload_to = 'articles/')
    image_name = models.TextField(max_length=50)
    description = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add= True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
    
    @classmethod    
    def get_image(cls):
        images = cls.objects.all()
        return images
    
class Location(models.Model):
    location = models.CharField(max_length= 20)
    
    def save_location(self):
        self.save()
    
    @classmethod
    def search_by_location(cls,search_term):
        results= cls.objects.filter(title__icontains = search_term)
        return results
    
    def __str__(self):
        return self.location
    
class Category(models.Model):
    category = models.CharField(max_length= 20)
    
    def save_category(self):
        self.save()
        
    @classmethod
    def search_by_category(cls,search_term):
        results= cls.objects.filter(title__icontains = search_term)
        return results
    
    def __str__(self):
        return self.category
    