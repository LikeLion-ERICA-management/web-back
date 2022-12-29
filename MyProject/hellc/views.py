from .models import *
from myApp.models import *
from rest_framework import viewsets
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import time, datetime, pytz

# Create your views here.
@api_view(["GET", "POST"])
def pet(request):
    serializer = []

    if request.method == "POST":
        pet = Pet()
        user_id = request.data["user_id"]
        user = CustomUser.objects.get(id = user_id)
        pet.user = user
        pet.name = request.data["name"]
        pet.save()
        
        serializer = PetSerializer(pet, context = {"request" : request})
        return Response(serializer.data)
    
    else:
        user_id = request.query_params["user_id"]
        pet = Pet.objects.get(id = user_id)
        serializer = PetSerializer(pet, context = {"request" : request})
        return Response(serializer.data)

@api_view(["GET", "POST"])
def calendar(request):
    serializer = []

    if request.method == "POST":
        user_id = request.data["user_id"]

        if Calendar.objects.get(user = user_id):
            return Response({"result": "Calender Already Exsit"}, status=400)

        try:
            pet = Pet.objects.get(user_id = user_id)
        except Pet.DoesNotExist:
            pet = Pet()
            user = CustomUser.objects.get(id = user_id)
            pet.user = user
            pet.name = "기본이름"
            pet.save()

        
        calendar = Calendar()

        calendar.user = CustomUser.objects.get(id = user_id)
        user_data = calendar.log
        user_data = json.loads(user_data)

        calendar.save()

        room = Room()
        room.user = CustomUser.objects.get(id = user_id)
        room.host = user_id
        room.save()

        serializer = CalendarSerializer(calendar, context = {"request" : request})
        return Response(serializer.data)
    else:
        try:
            user_id = request.query_params["user_id"]
            calendar =  Calendar.objects.get(user = user_id)
            
            user_data = calendar.log
            user_data = json.loads(user_data)

            year = request.query_params["year"]
            month = request.query_params["month"]

            if not (year in user_data):
                user_data[year] = {}
            if not(month in user_data[year]):
                user_data[year][month] = [{} for _ in range(31)]
            res = user_data[year][month]

            calendar.log = json.dumps(user_data)
            calendar.save()

            return Response({"result" : res})

        except Calendar.DoesNotExist:
            return Response({"result" : "user_id doesn't "})


@api_view(["POST"])
def calendar_record(request):
    serializer = []

    user_id = request.data["user_id"]
    try:
        calendar:Calendar = Calendar.objects.get(user = user_id)
        
        if(calendar.is_recording):
            start_time = calendar.start_time
            end_time = int(time.time())

            workout_time = end_time - start_time
            calendar.total_time += workout_time

            pet = Pet.objects.get(user = calendar.user)
            pet.level = calendar.total_time // 5
            pet.save()

            user_data = calendar.log
            user_data = json.loads(user_data)
            tz = pytz.timezone('Asia/Seoul')
            curTimeData = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
            year = curTimeData.year
            month = curTimeData.month
            day = curTimeData.day

            workLog = WorkLog()
            workLog.start_time = calendar.start_time
            workLog.end_time = end_time
            workLog.is_arm = request.data["is_arm"] 
            workLog.is_chest = request.data["is_chest"] 
            workLog.is_shoulder = request.data["is_shoulder"] 
            workLog.is_leg = request.data["is_leg"] 
            workLog.is_back = request.data["is_back"]
            workLog.gym_name = request.data["gym_name"]
            workLog.year = year
            workLog.month = month
            workLog.date = day
            workLog.save()

            if not ("total_time" in user_data[str(year)][str(month)][day-1]):
                user_data[str(year)][str(month)][day-1]["total_time"] = 0
            if not ("log" in user_data[str(year)][str(month)][day-1]):
                user_data[str(year)][str(month)][day-1]["log"] = []
            user_data[str(year)][str(month)][day-1]["total_time"] += workout_time

            dt_start_time = datetime.datetime.fromtimestamp(start_time)
            dt_end_time = datetime.datetime.fromtimestamp(end_time)

            
            start_string = dt_start_time.astimezone(tz).strftime("%H:%M")
            end_string = dt_end_time.astimezone(tz).strftime("%H:%M")
            
            
            worklog_value = {
                "start_time" : start_string,
                "end_time" : end_string,
                "gym_name" : workLog.gym_name,
                "is_arm" : workLog.is_arm,
                "is_leg" : workLog.is_leg,
                "is_shoulder" : workLog.is_shoulder,
                "is_back" : workLog.is_back,
                "is_chest" : workLog.is_chest,
            }
            user_data[str(year)][str(month)][day-1]["log"].append(worklog_value)

            calendar.is_recording = False
            calendar.start_time = 0 
            calendar.log = json.dumps(user_data)
            calendar.save()

            return Response({"result" : "end", "workout_time" : workout_time}, status = 200)
        else:
            calendar.is_recording = True
            calendar.start_time = int(time.time())
            calendar.save()
            return Response({"result" : "start", "workout_time" : 0}, status = 200)


    except Calendar.DoesNotExist:
        return Response({"result" : "Calendar's user_id dose not exist."})

@api_view(["GET", "POST"])
def room(request):
    serializer = []
    try:
        user_id = 1
        if(request.method == "POST"):
            user_id = request.data["user_id"]
        else:
            user_id = request.query_params["user_id"]
        room = Room.objects.get(id = user_id)
    except Room.DoesNotExist:
        return Response({"result" : "Room does not exist"})

    # 방문
    if (request.method == "POST"):
        guest_id = request.data["guest_id"]
        
        if (room.guest_number >= 4):
            return Response({"result" : "Room is Full!"})
        else:
            if (room.guest_number == 0):
                room.guest1 = guest_id
            elif room.guest_number == 1:
                room.guest2 = guest_id
            elif room.guest_number == 2:
                room.guest3 = guest_id
            elif room.guest_number == 3:
                room.guest4 = guest_id
    
            room.guest_number += 1
    user = CustomUser.objects.get(id = room.host)
    host_pet = Pet.objects.get(user = user)

    res = {
        "host" : {
            "name" : host_pet.name,
            "level" : host_pet.level
        },
        "guest_number" : room.guest_number,
        "guest1" : {},
        "guest2" : {},
        "guest3" : {},
        "guest4" : {},
    }    
    
    guests = ["guest1","guest2","guest3","guest4"]
    room_guests = [room.guest1, room.guest2, room.guest3, room.guest4]

    for index in range(room.guest_number):
        user = CustomUser.objects.get(id = room_guests[index])
        pet = Pet.objects.get(user=user)
        res[guests[index]]["name"] = pet.name
        res[guests[index]]["level"] = pet.level

    return Response(res)


