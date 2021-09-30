from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.contrib.auth.models import User
# Create your views here.


def register(req):
    if req.method == 'POST':
        username = req.POST['username']
        fname = req.POST['fname']
        lname = req.POST['lname']
        email = req.POST['email']
        password = req.POST['password']
        c_pass = req.POST['c_pass']
        if password != c_pass:
            messages.info(req, "Password Mismatch")
            return redirect('register')
        else:
            try:
                if User.objects.filter(email=email).exists():
                    messages.info(req, 'Email Already Exist')
                    return redirect('register')
                elif User.objects.filter(username=username).exists():
                    messages.info(req, 'Username Already Exist')
                    return redirect('register')
                user = User.objects.create_user(username=username, password=password, first_name=fname, last_name=lname, email=email)
                user.save()
                print('User registered')
                return redirect('login')
            except Exception:
                messages.info(req, 'unable to register')
                return redirect('register')
    return render(req, 'register.html')

def login(req):
    if req.method=="POST":
        username=req.POST['username']
        password=req.POST['password']
        user=auth.authenticate(req,username=username,password=password)
        if user is not None:
            auth.login(req,user)
            return redirect('/')
        else:
            messages.info(req,'username or password incorrect')
            return redirect('login')
    return render(req,'login.html')

def logout(req):
    auth.logout(req)
    return redirect('/')