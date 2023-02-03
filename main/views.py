from django.shortcuts import render
from .models import *

def show_hospital(request):
    return render(request, 'main/show_hospital.html')

def bd(request):
    return render(request, 'main/bd.html')
