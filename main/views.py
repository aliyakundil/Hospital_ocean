from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages                         #  Для распознования
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, UserLoginForm


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'login user')
            return redirect('/')
        else:
            messages.error(request, 'Error login')
    else:
        form = UserLoginForm()
    return render(request, 'register/login.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Register Success')
            return redirect('/')
        else:
            messages.error(request, 'Register Error')
    else:
        form = UserRegisterForm()
    return render(request, 'register/register.html', {'form':form})
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
