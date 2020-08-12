from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import *
from django.core.mail import send_mail


# Create your views her
def index(request):
    return render(request,'index.html')
def submit(request):
    if request.method=="POST":
         #print("hello from is submitted")
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        subject=request.POST["subject"]
        message=request.POST["message"]

        Resume_info = Resume(fname=fname,lname=lname,email=email,subject=subject,message=message)
        Resume_info.save()
        #send an email
        send_mail(
            subject+fname+lname, #subject
            message, #message
            email, #from email
            ['mohitedinesh363@gmail.com'],#to email
         )
        return render(request,'index.html', {'fname': fname})
    else:
        return render(request,'index.html')
