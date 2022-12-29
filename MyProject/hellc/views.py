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
        user_id = request.data["user_id"]
        pet = Pet.objects.get(id = user_id)
        serializer = PetSerializer(pet, context = {"request" : request})
        return Response(serializer.data)

@api_view(["GET", "POST"])
def calendar(request):
    serializer = []

    if request.method == "POST":
        user_id = request.data["user_id"]
        pet = Pet.objects.get(user_id = user_id)
        
        calendar = Calendar()

        calendar.user = CustomUser.objects.get(id = user_id)
        calendar.save()

        room = Room()
        room.user = request.data["user_id"]
        room.host = pet
        room.save()

        serializer = CalendarSerializer(calendar, context = {"request" : request})
        return Response(serializer.data)
    else:
        try:
            user_id = request.data["user_id"]
            calendar =  Calendar.objects.get(user = user_id)
            
            user_data = calendar.log
            user_data = json.loads(user_data)

            year = request.data["year"]
            month = request.data["month"]

            res = user_data[year][month]

            return Response({"result" : res})

        except Calendar.DoesNotExist:
            return Response({"result" : "user_id doesn't "})


@api_view(["POST"])
def calendar_record(request):
    serializer = []

    user_id = request.data["user_id"]
    try:
        calendar:Calendar = Calendar.objects.find(user = user_id)
        
        if(calendar.is_recording):
            start_time = calendar.start_time
            end_time = int(time.time())

            workout_time = end_time - start_time
            calendar.total_time += workout_time

            pet = Pet.objects.get(user = calendar.user)
            pet.level = calendar.total_time // 1000000
            pet.save()

            user_data = calendar.log
            user_data = json.loads(user_data)
            
            curTimeData = datetime.datetime.now(pytz.timezone('UTC+09:00'))
            year = curTimeData.year
            month = curTimeData.month
            day = curTimeData.day
            user_data[str(year)][str(month)][day-1] = workout_time

            calendar.is_recording = False
            calendar.start_time = 0 
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

    # 방문
    if (request.method == "POST"):
        user_id = request.data["user_id"]
        guest_id = request.data["guest_id"]
        
        room = Room.objects.get(id = user_id)
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
    
    host_pet = Pet.objects.get(user_id = room.host)

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
        pet = Pet.objects.get(user_id = room_guests[index])
        res[guests[index]]["name"] = pet.name
        res[guests[index]]["level"] = pet.level

    return Response(res)


