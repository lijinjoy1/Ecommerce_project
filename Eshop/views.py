from django.shortcuts import render
from .models.products import Products
from .models.category import Category

# Create your views here.
def homepage(request):
    product = None
    categories= Category.get_all_categories()
    categoryID=request.GET.get('category')
    if categoryID:
        product=Products.get_all_products_by_id(categoryID)
    else:
        product = Products.get_all_products()
    context ={
        'products':  product ,
        'category': categories,
    }
    return render(request,'home.html', context)