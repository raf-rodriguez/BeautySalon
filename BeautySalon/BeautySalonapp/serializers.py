from rest_framework import serializers
from .models import Client, Service, Appointment, Booking
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UploadedFile
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['name', 'email']
        filter_backends = [filters.SearchFilter]
        search_fields = ['name', 'email']
        filter_backends = [filters.OrderingFilter]
        ordering_fields = ['name', 'email']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__' 
        extra_kwargs = {
            'url': {'view_name': 'service-detail', 'lookup_field': 'pk'}
        }

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'client-detail', 'lookup_field': 'pk'}
        }

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = '__all__'