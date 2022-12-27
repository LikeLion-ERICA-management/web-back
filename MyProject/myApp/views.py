from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializer import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

import datetime

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
    opening = Opening.objects.latest()
    data = {
        "questions": [
                    opening.question1,
                    opening.question2,
                    opening.question3,
                    opening.question4,
                    opening.question5,
                    opening.question6,
                    opening.question7,
                    opening.question8,
                    opening.question9,
                    opening.question10,
                ]
    }
    
    return Response(data,status=200)

@api_view(["GET"])
def application_all(request):
    serializer = []

    applications = Application.objects.all()
    serializer = ApplicationSerializer(applications, context = {"request" : request}, many = True)
    
    return Response(serializer.data)


    
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

@api_view(["GET","POST"])
def work(request):
    serializer = []
    if request.method == "POST":
        work = Work()
        work.duration = request.data["duration"]
        work.title = request.data["title"]
        work.date = request.data["date"]
        work.image = request.data["image"]
        work.save()
        serializer = WorkSerializer(work, context = {"request":request})     
    else:
        works = Work.objects.all()
        serializer = WorkSerializer(works, context = {"request":request}, many = True)
    return Response(serializer.data)

@api_view(["POST"])
def delete_work(request):
    serializer = []
    try:
        work_id = request.data["id"]
        work = Work.objects.get(id = work_id)
        work.delete()
    except Work.DoesNotExist:
        return Response({"response":"Work's ID dose not exist."}, status=404)

    works = Work.objects.all()
    serializer = WorkSerializer(works, context = {"request": request}, many = True)
    
    return Response(serializer.data)


@api_view(["GET","POST"])
def waiter(request):
    serializer = []
    
    if request.method == "POST":
        waiter = Waiter()

        waiter.name = request.data["name"]
        waiter.email = request.data["email"]
        waiter.save()
    
    waiters = Waiter.objects.all()
    serializer = WaiterSerializer(waiters, context = {"request" : request}, many = True)
    
    return Response(serializer.data)

@api_view(["GET", "POST"])
def faq(request):
    serializer = []
    
    if request.method == "POST":
        faq = FAQ()

        faq.question_type = request.data["question_type"]
        faq.question = request.data["question"]
        faq.answer = request.data["answer"]

        faq.save()
    
    faqs = FAQ.objects.all()
    serializer = FAQSerializer(faqs, context = {"request" : request}, many = True)
    
    return Response(serializer.data)

@api_view(["POST"])
def update_faq(request):
    serializer = []

    question_id = request.data["question_id"]
    try:
        question = FAQ.objects.get(id = question_id)
        
        question.question_type = request.data["question_type"]
        question.question = request.data["question"]
        question.answer = request.data["answer"]
        
        question.save()
    except FAQ.DoesNotExist:
        return Response({"result" : "Question id dose not exist"}, status = 404)

    questions = FAQ.objects.all()
    serializer = FAQSerializer(questions, context = {"request" : request}, many = True)
    
    return Response(serializer.data)


@api_view(["POST"])
def delete_faq(request):
    serializer = []

    question_id = request.data["question_id"]
    try:
        question = FAQ.objects.get(id = question_id)
        
        question.delete()
    except FAQ.DoesNotExist:
        return Response({"result" : "Question id dose not exist"}, status = 404)

    questions = FAQ.objects.all()
    serializer = FAQSerializer(questions, context = {"request" : request}, many = True)
    
    return Response(serializer.data)

@api_view(["GET","POST"])
def opening(request):
    serializer = []

    if request.method == "POST":
        if Opening.objects.latest.is_opened:
            return Response({"result" : "현재 공고가 열려 있습니다"}, status = 400)

        start_date = request.data["start_date"]
        end_date = request.data["end_date"]
        
        sd = datetime.strptime(start_date, '%Y-%m-%d')
        ed = datetime.strptime(end_date, '%Y-%m-%d')

        if(ed - sd <= 0):
            return Response({"result" : "시작 날짜가 종료 날짜보다 같거나 이후입니다."},status=403)
        
        opening = Opening()
        opening.start_date = start_date
        opening.end_date = end_date
        opening.generation = request.data["generation"]

        req_questions = request.data["questions"]
        questions = [
            opening.question1,
            opening.question2,
            opening.question3,
            opening.question4,
            opening.question5,
            opening.question6,
            opening.question7,
            opening.question8,
            opening.question9,
            opening.question10,
        ]

        for i in range(10):
            questions[i] = req_questions[i]

        opening.save()
    
    openings = Opening.objects.all()
    serializer = OpeningSerializer(openings,context = {"request" : request}, many = True)

    return Response(serializer.data)

@api_view(["GET"])
def detail_opening(request):
    serializer = []
    opening_id = request.data["opening_id"]
    try:
        opening = Opening.objects.get(id = opening_id)
        response = {
                "id": opening.id,
                "generation": opening.generation,
                "title": opening.title,
                "start_date": opening.start_date,
                "end_date": opening.end_date,
                "is_opened": opening.is_opened,
                "questions": [
                    opening.question1,
                    opening.question2,
                    opening.question3,
                    opening.question4,
                    opening.question5,
                    opening.question6,
                    opening.question7,
                    opening.question8,
                    opening.question9,
                    opening.question10,
                ]
            }
        return Response(response, status=200)
    except Opening.DoesNotExist:
        return Response({"result" : "Opening id dose not exist"}, status = 404)

@api_view(["POST"])
def update_opening(request):
    serializer = []

    try:
        start_date = request.data["start_date"]
        end_date = request.data["end_date"]
        
        sd = datetime.strptime(start_date, '%Y-%m-%d')
        ed = datetime.strptime(end_date, '%Y-%m-%d')

        if(ed - sd <= 0):
            return Response({"result" : "시작 날짜가 종료 날짜보다 같거나 이후입니다."},status=400)
        
        opening_id = request.data["opening_id"]
        opening = Opening.objects.get(id=opening_id)

        opening.start_date = start_date
        opening.end_date = end_date
        opening.generation = request.data["generation"]

        req_questions = request.data["questions"]
        questions = [
            opening.question1,
            opening.question2,
            opening.question3,
            opening.question4,
            opening.question5,
            opening.question6,
            opening.question7,
            opening.question8,
            opening.question9,
            opening.question10,
        ]

        for i in range(10):
            questions[i] = req_questions[i]

        opening.save()
    except Opening.DoesNotExist:
        return Response({"result" : "Opening id dose not exist"}, status = 404)
    
    openings = Opening.objects.all()
    serializer = OpeningSerializer(openings,context = {"request" : request}, many = True)

    return Response(serializer.data)

@api_view(["POST"])
def delete_opening(request):
    serializer = []

    try:
        opening_id = request.data["opening_id"]
        opening = Opening.objects.get(id=opening_id)
    
        opening.delete()
    except Opening.DoesNotExist:
        return Response({"result" : "Opening id dose not exist"}, status = 404)
    
    openings = Opening.objects.all()
    serializer = OpeningSerializer(openings,context = {"request" : request}, many = True)

    return Response(serializer.data)