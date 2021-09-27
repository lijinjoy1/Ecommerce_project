from django.contrib import admin
from .models.products import Products
from .models.category import Category
# Register your models here.

class adminproducts(admin.ModelAdmin):
    list_display=['name','price','category','description','image']
admin.site.register(Products,adminproducts)


class admincategory(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Category,admincategory)