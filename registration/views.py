from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ApplicantSerializer
from .models import Applicants

# Create your views here.

class ApplicantsViewSet(viewsets.ModelViewSet):
    queryset=Applicants.objects.all().order_by('-id')
    serializer_class=ApplicantSerializer
