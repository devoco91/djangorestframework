# from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Product(models.Model):
    image=models.ImageField(upload_to='img')
    name=models.CharField(max_length=200, null=True)
    description=models.TextField(blank=True)
    price=models.CharField(max_length=200, null=True)
    date=models.DateTimeField(auto_now_add=True)