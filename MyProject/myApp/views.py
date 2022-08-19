from django.shortcuts import render
from .models import Blog
from rest_framework import viewsets
from .serializer import BlogSerializer


# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
