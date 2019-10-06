# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Editor,Images,tags,Location,Category


class ImagesAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

# Register your models here.
admin.site.register(Editor)
admin.site.register(Images,ImagesAdmin)
admin.site.register(tags)
admin.site.register(Location)
admin.site.register(Category)
