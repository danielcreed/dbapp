from turtle import title
from django.db import models
from staff.models import Staff

# Create your models here.

class Listing(models.Model):
    User = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, blank=True)
    VendorName = models.CharField(max_length=200)
    Website = models.CharField(max_length=100 )
   # Country = models.BooleanField(default=False)
    Countries = (
       ('Canada', 'Canada'),
       ('USA', 'USA'),
    )
    Country = models.CharField(max_length=20, choices=Countries, blank=True)
    Category = models.CharField(max_length=100)
    Ranking = models.IntegerField(blank=True)
    desciption = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.VendorName