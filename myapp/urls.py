from unicodedata import name
from django.urls import path, include
from . import views
urlpatterns = [
    # path("",views.mainpage,name='index'),
    path("",views.registerpage,name="register"),
    path("register/",views.UserRegister,name="registerdata"),
    path("login/",views.Loginpage,name="loginpage"),
    path("loginuser/",views.Loginuser,name="Loginuser"),
    path("contactform/",views.contactForm,name="contactForm")
    
]