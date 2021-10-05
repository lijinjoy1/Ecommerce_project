from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from Eshop.models.signupcustomer import Signupcustomer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postdata = request.POST
        first_name = postdata.get('firstname')
        last_name = postdata.get('lastname')
        email = postdata.get('email')
        city = postdata.get('city')
        phone = postdata.get('phone')
        password = postdata.get('password')

        # validation
        value = {
            'firstname': first_name,
            'lastname': last_name,
            'email': email,
            'city': city,
            'phone': phone
        }
        error_message = None
        signupcustomer = Signupcustomer(first_name=first_name,
                                        last_name=last_name,
                                        email=email,
                                        city=city,
                                        phone=phone,
                                        password=password)

        error_message = self.validate_customer(signupcustomer)

        # saving after validation
        if (not error_message):
            signupcustomer.password = make_password(signupcustomer.password)
            signupcustomer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value,
            }
        return render(request, 'signup.html', data)

    def validate_customer(self, signupcustomer):
        error_message = None
        if (not signupcustomer.first_name):
            error_message = "First name is required.....!!!!"
        elif len(signupcustomer.first_name) < 3:
            error_message = "First name must me 3 character or long....!!!"
        elif (not signupcustomer.last_name):
            error_message = "Second name is required.....!!!!"
        elif len(signupcustomer.last_name) < 3:
            error_message = "Second name must me 3 character or long....!!!"

        elif len(signupcustomer.email) < 3:
            error_message = "email must me 3 character or long....!!!"

        elif (not signupcustomer.city):
            error_message = "City is required.....!!!!"
        elif (not signupcustomer.phone):
            error_message = "Phone number is required.....!!!!"
        elif len(signupcustomer.phone) < 10:
            error_message = "Phone number must me 10 character....!!!"
        elif (not signupcustomer.password):
            error_message = "password is required.....!!!!"
        elif len(signupcustomer.password) < 3:
            error_message = "password must me 3 character or long....!!!"
        elif signupcustomer.email_exsist():
            error_message = "Email is already registerd...!!!"
        return error_message
