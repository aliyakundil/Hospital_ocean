from django.db import models
from django.urls import reverse

class Hospital(models.Model):
    okpo = models.CharField(max_length=222, unique=True)
    chiefphysician = models.CharField(max_length=222, unique=True)
    hirurg =  models.CharField(max_length=222)
    therapists = models.CharField(max_length=222)
    nurses = models.CharField(max_length=222)
    patients = models.CharField(max_length=222)





    def __str__(self):
        return self.okpo
