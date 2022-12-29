from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ("name", "level", "user")

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ("user","log",)

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Room
        fields = ("user", "host", "guest_number", "guest1", "guest2", "guest3", "guest4")
    