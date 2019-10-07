# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    
    def __str__(self):
        return self.first_name
    
    def save_editor(self):
        self.save()
    
    class Meta:
        ordering = ['first_name']
        verbose_name = 'Editor'
        verbose_name_plural = 'Editors'

class tags(models.Model):
    name = models.CharField(max_length= 20)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

class Location(models.Model):
    name = models.CharField(max_length= 20)
    
    def save_location(self):
        self.save()
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length= 20)
    
    def save_category(self):
        self.save()
    
    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length=50)
    description = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add= True)
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
    
    @classmethod    
    def get_image(cls):
        new = cls.objects.all()
        return new
    
    @classmethod
    def search_by_category(cls,search_term):
        new= cls.objects.filter(image_category__name__icontains = search_term)
        return new
    
    @classmethod
    def search_by_location(cls,search_term):
        new= cls.objects.filter(image_location__name__icontains = search_term)
        return new
    
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
