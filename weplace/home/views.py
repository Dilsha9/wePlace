from django import forms
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CompanyRegister, Student
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import StudentForm
# Create your views here.
def index(request):
    return render(request, 'index.html')
def loginmain(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def applystudent(request):
    dict_apply={
        'apply': CompanyRegister.objects.all()
    }
    return render(request, 'applystudent.html',dict_apply)
def studentsignup(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        verify = request.POST['verify']
        if password==verify:
            myuser = User.objects.create_user(username=username,email=email,password=password)
            myuser.first_name = fname
            myuser.last_name= lname

            myuser.save()
            messages.success(request,"Successfully Registered")
            return redirect('studentlogin')
        else:
            messages.error(request,"Bad Credentials")
            return redirect('home')
    return render(request, 'studentsignup.html')
def studentlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(username=username,email=email,password=password)

        if user is not None:
            login(request, user)
            fname=user.first_name
            return render(request,'myprofile.html',{'fname': fname})
        else:
            messages.error(request,"Bad Credentials")
            return redirect('home')
        
    return render(request, 'studentlogin.html')
def myprofile(request):
    if request.method=='POST':
        form= StudentForm(request.POST)
        if form.is_valid():
            form.save()
    form= StudentForm()
    dict_form={
        'form': form
    }
    return render(request, 'myprofile.html',dict_form)
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')


