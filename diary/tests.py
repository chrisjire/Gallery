# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Image,Editor,tags,Category,Location

# Create your tests here.
class EditorTestClass(TestCase):
    def setUp(self):
        self.mary=  Editor(first_name = 'mary', last_name ='had', email ='mary@gmail.com')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.mary,Editor))
        
    def test_save_method(self):
        self.mary.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
        
class tagsTestClass(TestCase):
    def setUp(self):
        self.world= tags(name='world')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.world,tags))
        

class LocationTestClass(TestCase):
    def setUp(self):
        self.London= Location(name='London')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.London,Location))
        
    def test_save_method(self):
        self.London.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
        
class CategoryTestClass(TestCase):
    def setUp(self):
        self.cool= Category(name='cool')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.cool,Category))
        
    def test_save_method(self):
        self.cool.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
        
