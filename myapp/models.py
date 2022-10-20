from email.message import Message
from django.db import models

# Create your models here.

class users(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)


class contact(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Subject = models.CharField(max_length=50)
    Message = models.CharField(max_length=150)
