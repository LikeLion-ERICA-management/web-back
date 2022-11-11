"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from myApp import views

from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'board',views.BlogViewSet)
router.register(r'paper',views.PaperViewSet)
router.register(r'paperadmin',views.PaperAdminViewSet)
router.register(r'actlog',views.ActLogViewSet)
router.register(r'notice',views.NoticeViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('dj-rest-auth/',include('dj_rest_auth.urls')),
    path('dj-rest-auth/register/',include('dj_rest_auth.registration.urls'))
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)