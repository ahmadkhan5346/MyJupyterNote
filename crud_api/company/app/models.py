from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    city = models.CharField(max_length=100)
