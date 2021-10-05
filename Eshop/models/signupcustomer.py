from django.db import models

class Signupcustomer(models.Model):
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email= models.EmailField()
    city= models.CharField(max_length=50)
    phone= models.CharField(max_length=15)
    password= models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Signupcustomer.objects.get(email=email)
        except:
            return False
        
    

    
    
    
    def email_exsist(self):
        if Signupcustomer.objects.filter(email=self.email):
            return True

        return False
