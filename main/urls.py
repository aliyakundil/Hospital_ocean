from django.urls import path
from .views import *

urlpatterns = [
   path('', show_hospital, name='show_hospital')
]