from django.shortcuts import redirect, render,redirect
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
        
        # validation
        value={
            'firstname':firstname,
            'lastname':lastname,
            'email':email,
            'city':city,
            'phone':phone
        }
        error_message= None
        if (not firstname):
            error_message="First name is required.....!!!!"
        elif len(firstname)<3:
            error_message="First name must me 3 character or long....!!!"
        elif (not lastname):
            error_message="Second name is required.....!!!!"
        elif len(lastname)<3:
            error_message="Second name must me 3 character or long....!!!"
        
        elif len(email)<3:
            error_message="email must me 3 character or long....!!!"
        
        elif (not city):
            error_message="City is required.....!!!!"
        elif (not phone):
            error_message="Phone number is required.....!!!!"
        elif len(phone)<10:
            error_message="Phone number must me 10 character....!!!"
        elif (not password):
            error_message="password is required.....!!!!"
        elif len(password)<3:
            error_message="password must me 3 character or long....!!!"
        

        
        

        
        



        # saving after validation
        if (not error_message):
            signupcustomer=Signupcustomer(first_name=firstname,
                                        last_name=lastname,
                                        email=email,
                                        city=city,
                                        phone=phone,
                                        password=password)
            signupcustomer.register()
            return redirect('homepage')
        else:
            data={
                    'error':error_message,
                    'values':value,
            }
            return render(request,'signup.html',data)
                


def about(request):
    return render(request,'about.html')