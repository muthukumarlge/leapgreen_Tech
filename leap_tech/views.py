from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import login,logout
from django.contrib import messages
# Create your views here.

def loginPage(request):
    return render(request,"login.html")

def loginUser(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        print(request.POST.get("username"))
        user=EmailBackEnd.authenticate(request,username=request.POST.get("username"),password=request.POST.get("password"))      
        if user!=None:
            login(request,user)
            return HttpResponseRedirect(reverse("itHome"))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")



def itHome(request):
    return render(request,"it_template/home.html")