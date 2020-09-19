from rest_framework import serializers
from PARK.models import Users
from django.db import connection
from django.core.validators import MaxValueValidator, MinValueValidator
def func():
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM PARK_users")
    y=cursor.fetchone()
    if int(y[0]) == 0:# if empty then fill the first i.e 1
        return 1
    if int(y[0]) == 10:# if full then  return 11
        return 11
    cursor.execute("SELECT MIN(slot_number) FROM PARK_users")
    x=cursor.fetchone()
    if int(x[0]) > 1:#if min is >1 then fill its prev.
        return int(x[0])-1
    cursor.execute("SELECT MAX(slot_number) FROM PARK_users")
    x=cursor.fetchone()
    if(int(x[0])==int(y[0])):#return max + 1 because all are full from 1 to max
        return int(x[0])+1
    #here we come because min=1 and there must be gap , so we will find that and fill
    cursor.execute("SELECT MAX(slot_number) FROM PARK_users WHERE slot_number-1 NOT IN (SELECT slot_number from PARK_users);")
    x=cursor.fetchone()
    return int(x[0])-1
class UsersSerializer(serializers.ModelSerializer):
    slot_number = serializers.IntegerField(required=False,default=func())#we have modified User class  conditon
    #validators=[MinValueValidator(1), MaxValueValidator(10)]
    class Meta:
        model = Users
        #fields will set tuple to be shown
        fields = '__all__'
        #fields =  ('car_number','slot_number')