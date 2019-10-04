# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

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
    
    