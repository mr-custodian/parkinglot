from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.db import models
#get list of all users
class UserList(APIView):#clearly UserList inherit APIView class
    def get(self , request):
        model=Users.objects.all()#take all objects i.e all entries from User class in 'model.py'
        serializer = UsersSerializer(model, many=True)#Serializeation of object
        return Response(serializer.data)
    # Park a Car :will take car_number and return slot_number
    def post(self, request):
        #Deserialization object , converting json type which is typed on server to its original from
        #on clicking post button this will start working
        serializer = UsersSerializer(data=request.data)#data from request entered in server which is post by button
        #post is "request.data" here which will be fetch to UserSerializer which will then convert back to original from
        #if (serializer.slot_number > 100):  # if slots are full then it will give value >100
         #   return Response('all slot are full please wait for some vacant slots', status=status.HTTP_412_PRECONDITION_FAILED)
        if(serializer.is_valid()):
            cnt=Users.objects.count()
            if(cnt==10):
                return Response('Data Overflow', status=status.HTTP_412_PRECONDITION_FAILED)
            serializer.save()#if data taken is good then it will be stored in database and return created data only
            #and not all the rows because here serializer.data is only for one entry
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#else it is error and bad request

class UserDetail(APIView):#clearly UserDetail inherit APIView class
    #Get the Car/Slot info : will take either a slot_number or car_number and return full info
    def get(self, request,number):
        try:
            if int(number)<=10:
                   model=Users.objects.get(slot_number=number)#model get whole User but slot_number is taken from url
                   #and then model search that slot_number in database and when found it store in model
            else:
                   model = Users.objects.get(car_number=number)  # model get whole User but car_number is taken from url
                   # and then model search that car_number in database and when found it store in model
        except Users.DoesNotExist:
            if int(number)>10:
                   return Response(f'Car with car number {number} is not found in database',status=status.HTTP_404_NOT_FOUND)
            return Response(f'slot with slot number {number} is already empty', status=status.HTTP_404_NOT_FOUND)
        serializer = UsersSerializer(model)#Serialization of object
        return Response(serializer.data)
    #Park a Car :will take car_number and return car_number
    def put(self, request,slot_number):# take from url and do the work
        try:
            model=Users.objects.get(slot_number=slot_number)
        except Users.DoesNotExist:
            return Response(f'User with {slot_number} is not found in database',status=status.HTTP_404_NOT_FOUND)

        serializer = UsersSerializer(model,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #Unpark Car:takes slot_number and delete the row
    def delete(self, request,number):
        try:
            model = Users.objects.get(car_number=number)
        except Users.DoesNotExist:
            return Response(f'User with slot number {number} is already empty', status=status.HTTP_404_NOT_FOUND)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)