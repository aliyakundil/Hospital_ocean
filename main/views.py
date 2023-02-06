from django.shortcuts import render
from .models import *

def show_hospital(request):
    hospital = Hospital.objects.all()
    c_physician = Chief_Physician.objects.all()
    therapist = Therapist.objects.all()
    nurse = Nurse.objects.all()
    patients = Patients.objects.all()
    return render(request, 'main/show_hospital.html', {'hospital':hospital,'c_physician':c_physician,'therapist':therapist, 'nurse':nurse, 'patients':patients})

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
