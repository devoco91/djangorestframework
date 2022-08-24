from django.db import models

# Create your models here.


class Contact_u(models.Model):
    name=models.CharField(max_length=200, null=True)
    email=models.EmailField(max_length=200, null=True)
    subject=models.CharField(max_length=200, null=True)
    phone=models.CharField(max_length=200, null=True)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name
