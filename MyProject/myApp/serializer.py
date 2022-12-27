from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

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

class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = ('applicant_name','applicant_email','applicant_major','context', 'reg_time','mod_time','year')

class PaperAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaperAdmin
        fields = ('year','is_opened','start_date','end_date')

class ActLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActLog
        fields = ('title', 'content', 'image')

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ('title','context','reg_time','mod_time','is_active')

class AboutSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = About
        fields = ('body','image',)

class WorkSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Work
        fields = ('id','title','duration','date','image',)
    
class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = ('id','name','email','create_date')

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('id','question_type','question','answer','create_date')
    
class OpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model=Opening
        fields=('id', 'generation', 'title', 'start_date', 'end_date','is_opened')
    