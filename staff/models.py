from distutils.command.upload import upload
from django.db import models
from datetime import datetime
# Create your models here.


class Staff(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    desription = models.TextField(blank=True)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    NewUser_Date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):

     return self.name