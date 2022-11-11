from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializer import *


# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class PaperViewSet(viewsets.ModelViewSet):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer

class PaperAdminViewSet(viewsets.ModelViewSet):
    queryset = PaperAdmin.objects.all()
    serializer_class = PaperAdminSerializer

class ActLogViewSet(viewsets.ModelViewSet):
    queryset = ActLog.objects.all()
    serializer_class = ActLogSerializer

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

