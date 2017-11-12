# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article, Place, Restaurant, Waiter, Publication
from .models import Author, Blog, Entry

admin.site.register(Article)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)
admin.site.register(Publication)
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Entry)