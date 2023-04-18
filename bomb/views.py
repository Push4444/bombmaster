from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def Login(request):
    if request.method=='POST':
        username=request.POST.get('name')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('Escape')
        else:
            return HttpResponse("Username or Password is incorrect !!!")
    return render (request,'Login.html')
@csrf_exempt
def Registration(request):
    if request.method=='POST':
        uname=request.POST.get('rusername')
        email=request.POST.get('remail')
        pass1=request.POST.get('rpassword1')
        pass2=request.POST.get('rpassword2')
        
        if pass1!=pass2:
            massage.warning(request,"Passwords doesnt match")
            return redirect('Registration.htm')
        else:    
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('Login')
    return render (request,'Registration.html')


def Clue1(request):
    return render(request,'Clue1.html')

def Clue2(request):
    return render(request,'Clue2.html')

def Clue3(request):
    return render(request,'Clue3.html')

def Clue4(request):
    return render(request,'Clue4.html')

def Clue5(request):
    return render(request,'Clue5.html')

def Clue6(request):
    return render(request,'Clue6.html')

def Escape1(request):
    return render (request,'Escape1.html')

def End(request):
    return render (request,'End.html')

def Dead(request):
    return render(request,'Dead.html')
