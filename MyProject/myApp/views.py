from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializer import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

@api_view(['GET'])
def check_apply(request):
    res = {
        "possible": True,
        "generation" : 10,
        "start" : "YYYY-MM-DD",
        "end" : "YYYY-MM-DD",
    }
    return JsonResponse(res)

@api_view(['GET'])
def check_before(request):
    name = request.data["name"]
    email = request.data["email"]
    is_applied = False

    try:
        application = Application.objects.get(email=email)
        is_applied = True
    except Application.DoesNotExist:
        pass
    
    res = {
        "name":str(name),
        "email":email,
        "is_applied":is_applied
    }
    
    return JsonResponse(res,json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])
def check_password(request):
    name = request.data["name"]
    email = request.data["email"]
    password = request.data["password"]
    is_verified = False

    try:
        app = Application.objects.get(email=email)
        if(password == app.password):
            is_verified = True
    except Application.DoesNotExist:
        res = {
            "result" : """Application Dose not Exist.
                          올바르지 못한 접근입니다."""
        }
        return JsonResponse(res,json_dumps_params={'ensure_ascii': False})

    res = {
        "name" : name,
        "email" : email,
        "is_verified" : is_verified
    }

    return JsonResponse(res,json_dumps_params={'ensure_ascii': False})

@api_view(["POST"])
def apply(request):
    name = request.data["name"]
    email = request.data["email"]

    try:
        app = Application(name=name,email=email)
        app.save()
    except:
        res = {
            "result" : """이미 존재하는 지원서입니다."""
        }
        return JsonResponse(res,json_dumps_params={'ensure_ascii': False},status = 404)

    res = {
        "name" : name,
        "email" : email,
    }

    return JsonResponse(res,json_dumps_params={'ensure_ascii': False})

@api_view(["GET"])
def load_application(request):
    email = request.data["email"]
    password = request.data["password"]
    applications = []

    try:
        app = Application.objects.get(email=email)
        if(password == app.password):
            applications.append(app.answer1)
            applications.append(app.answer2)
            applications.append(app.answer3)
            applications.append(app.answer4)
            applications.append(app.answer5)
            applications.append(app.answer6)
            applications.append(app.answer7)
            applications.append(app.answer8)
            applications.append(app.answer9)
            applications.append(app.answer10)
        else:
            return JsonResponse({"result" : "비밀번호가 틀렸습니다."},json_dumps_params={'ensure_ascii': False})
    except Application.DoesNotExist:
        res = {
            "result" : """Application Dose not Exist.
                          올바르지 못한 접근입니다."""
        }
        return JsonResponse(res,json_dumps_params={'ensure_ascii': False})
    res = {
        "applications": applications
    }

    return JsonResponse(res,json_dumps_params={'ensure_ascii': False})

@api_view(["POST"])
def update_application(request):
    name = request.data["name"]
    phone_number = request.data["phone_number"]
    email = request.data["email"]
    major = request.data["major"]
    student_id = request.data["student_id"]
    applications = request.data["applications"]
    password = request.data["password"]

    try:
        app = Application.objects.get(email=email)
        app.major = major
        app.phone_number = phone_number
        app.student_id = int(student_id)
        app.password = int(password)
        app.answer1 = applications[0]
        app.answer2 = applications[1]
        app.answer3 = applications[2]
        app.answer4 = applications[3]
        app.answer5 = applications[4]
        app.answer6 = applications[5]
        app.answer7 = applications[6]
        app.answer8 = applications[7]
        app.answer9 = applications[8]
        app.answer10 = applications[9]
        app.save()
    except Application.DoesNotExist:
        res = {
            "result" : "존재하지 않는 이메일입니다."
        }
        return JsonResponse(res,json_dumps_params={'ensure_ascii': False})
    
    res = {
        "name" : app.name,
        "phone_number" : app.phone_number,
        "email" : app.email,
        "major" : app.major,
        "student_id" : app.student_id,
        "applications" : request.data["applications"]
    }

    return JsonResponse(res,json_dumps_params={'ensure_ascii': False})

@api_view(["GET"])
def load_application_questions(request):
    res = {
        "questions" : ["1","2","3","4","5","6","7","8","9","10"]
    }

    return JsonResponse(res,json_dumps_params={'ensure_ascii': False})
    
@api_view(["GET","POST"])
def about(request):
    about = About.objects.latest()
    if request.method == "POST":
        body = request.data["body"]
        image = request.data["image"]
        about.body = body
        about.image = image
        about.save()
    serializer = AboutSerializer(about,context={"request":request})
    return Response(serializer.data)
