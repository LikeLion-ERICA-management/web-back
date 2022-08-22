from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog, CustomUser

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ['title','context']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email','last_login','date_joined','is_staff')

