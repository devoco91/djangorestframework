from rest_framework import serializers
from .models import Contact_u
class Contact_usSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_u
        fields = ['id', 'name',  'email', 'subject', 'phone', 'message']