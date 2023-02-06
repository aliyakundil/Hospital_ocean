from django.urls import path
from .views import *

urlpatterns = [
   path('', show_hospital, name='show_hospital'),
   path('bd/', bd, name='bd'),
   path('about/', about, name='about'),
   path('services/', services, name='services'),
   path('doctors/', doctors, name='doctors'),
   path('price/', price, name='price'),
   path('testimonials/', testimonials, name='testimonials'),
   path('contact/', contact, name='contact'),
]