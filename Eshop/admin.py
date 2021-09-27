from django.contrib import admin
from .models.products import Products
# Register your models here.

class adminproducts(admin.ModelAdmin):
    list_display=('name','price','description','image')
admin.site.register(Products,adminproducts)