from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password
from Eshop.models.signupcustomer import Signupcustomer
from django.views import View


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Signupcustomer.get_customer_by_email(email)

        # to checkpassword
        error_message = None
        value = {
            'email': email
        }
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return redirect('homepage')
            else:
                error_message = "Email or Password Invalid....!!"
        else:
            error_message = "Email or Password Invalid....!!"

        context = {
            'error': error_message,
            'values': value
        }
        print(customer)
        print(email, password)
        return render(request, 'login.html', context)