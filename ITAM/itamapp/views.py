from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm

# Create your views here.

def home(request):
    return render(request, 'itamapp/index.html')