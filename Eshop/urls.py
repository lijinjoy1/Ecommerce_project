from django.urls import path
from .views import Homepage_view,login_view,signup_view

urlpatterns = [

    path('',Homepage_view.Homepage.as_view(),name='homepage'),
    path('signup/',signup_view.Signup.as_view(),name='signup'),
    path('login/',login_view.Login.as_view(), name='login'),

    path('about/',Homepage_view.About.as_view(),name='about')

]