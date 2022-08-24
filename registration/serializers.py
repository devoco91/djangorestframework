from .models import Applicants
from rest_framework import serializers



class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Applicants
        # fields= '__all__'
        fields= ['id','firstname', 'lastname', 'email', 'phone','address','course','center','mode']