from django.shortcuts import render, redirect
from .models import *
from .forms import *

def VerIndex(request):
    return render(request, "index.html")