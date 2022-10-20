from django.shortcuts import render
from .models import *
# Create your views here.

def mainpage(request):
    return render(request,"myapp/index.html")

def registerpage(request):
    return render(request,"myapp/register.html")


def UserRegister(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['Contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        # first we validate if the user is already exists or not

        user = users.objects.filter(Email = email)

        if user:
            message = "User already exits"
            return render(request,"myapp/register.html",{'msg':message})
        else:
            if password == cpassword:
                newuser = users.objects.create(Firstname = fname,Lastname = lname,Email=email,Contact=contact,Password=password)
                message = "User registered successfully"
                return render(request,"myapp/login.html",{'msg':message})
            else:
                message = "Password entered is not matched"
                return render(request,"myapp/register.html",{'msg':message})


def Loginpage(request):
    return render(request,"myapp/login.html")


def Loginuser(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']

        #checking email with Database
        try:
            user = users.objects.get(Email = email)
            # print(user)
        except users.DoesNotExist:
            user = None
        if user:
            if user.Password == password:
                request.session['Firstname'] = user.Firstname
                request.session['Lastname'] = user.Lastname
                request.session['Emailid'] = user.Email
                return render(request,"myapp/home.html")
            else:
                message = "Password does not match"
                return render(request,"myapp/login.html",{'msg':message})
        else:
            message = "User does not exist"
            return render(request,"myapp/login.html",{'msg':message})


def contactForm(request):
    if request.method=='POST':
        firstname = request.session['Firstname']
        email = request.session['Emailid']
        subject = request.POST['subject']
        message = request.POST['message']
        contactuser = contact.objects.create(Name = firstname,Email=email,Subject=subject,Message=message)
        message = "Message Sended successfully"
        return render(request,"myapp/home.html",{'msg':message})