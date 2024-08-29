from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login

def index(request):
    Username = request.POST.get("username")
    Password = request.POST.get("password")
    user = authenticate(username=Username, password=Password)
    if user is not None:
        login(request, user)
    return render(request,"index.html")

# Create your views here.
