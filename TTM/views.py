from django.shortcuts import render

def homepage(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def register(request):
    return render(request,"register.html")