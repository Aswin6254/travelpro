from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method =='POST':
        user01=request.POST['username']
        pass01=request.POST['password']
        user=auth.authenticate(username=user01,password=pass01)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid user")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        v1 = request.POST['username']
        v2 = request.POST['firstname']
        v3 = request.POST['lastname']
        v4 = request.POST['email']
        v5 = request.POST['password']
        v6 = request.POST['confirm password']
        if v5==v6:
            if User.objects.filter(username=v1).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=v4).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
               u=User.objects.create_user(username=v1,password=v5,first_name=v2,last_name=v3,email=v4)

               u.save();
               return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')