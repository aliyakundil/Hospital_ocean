from django.shortcuts import render
from .models import *

def show_hospital(request):
    return render(request, 'main/show_hospital.html')

def bd(request):
    return render(request, 'main/bd.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def doctors(request):
    return render(request, 'main/doctors.html')

def price(request):
    return render(request, 'main/price.html')

def testimonials(request):
    return render(request, 'main/testimonials.html')

def contact(request):
    return render(request, 'main/contact.html')
