from django.shortcuts import render,HttpResponse
from .models.products import Products
from .models.category import Category
from .models.signupcustomer import Signupcustomer

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

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        postdata= request.POST
        firstname=postdata.get('firstname')
        lastname=postdata.get('lastname')
        email=postdata.get('email')
        city=postdata.get('city')
        phone=postdata.get('phone')
        password=postdata.get('password')
        print(firstname,lastname,email,city,phone,password)
        signupcustomer=Signupcustomer(first_name=firstname,
                                      last_name=lastname,
                                      email=email,
                                      city=city,
                                      phone=phone,
                                      password=password)
        signupcustomer.register()
        return HttpResponse('success')