from django.shortcuts import render
from Eshop.models.products import Products
from Eshop.models.category import Category

from django.views import View


# Create your views here.
class Homepage(View):
    def get(self, request):

        product = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            product = Products.get_all_products_by_id(categoryID)
        else:
            product = Products.get_all_products()
        context = {
        'products': product,
        'category': categories,
        }
        return render(request, 'home.html', context)


class About(View):
    def get(self, request):
        return render(request, 'about.html')