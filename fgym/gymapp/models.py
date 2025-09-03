from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='employee_pictures/', blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
    
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name

