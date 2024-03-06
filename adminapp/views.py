from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

from .models import Admin, Register


# Create your views here.
def ttmhome(request):
    return render(request, "ttmhome.html")
def checkadminlogin(request):
    if request.method == "POST":
        adminuname = request.POST["uname"]
        adminpwd = request.POST["pwd"]
        flag=Admin.objects.filter(username=adminuname,password=adminpwd).values()
        if flag:
            return render(request, "ttmhome.html")
        else:
            return render(request, "loginfail.html")

def checkRegistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            if Register.objects.filter(username=uname).exists():
                messages.info(request , "username existing...")
                return render(request,"register.html")
            elif Register.objects.filter(email=email).exists():
                messages .info(request, "email existing...")
                return render(request, "register.html")
            else:
                user = Register.objects.create(name=name,address=addr,email=email,phno=phno,username=uname,password=pwd)
                user.save()
                messages.info(request ," usercreated...")
                return render(request, "login.html")
        else:
            messages.info(request, "password is not matching...")
            return render(request, "register.html")
