from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Contact_usSerializer
from .models import Contact_u
class ContactViewSet(viewsets.ModelViewSet):
    queryset=Contact_u.objects.all().order_by('-id')
    serializer_class=Contact_usSerializer
    
