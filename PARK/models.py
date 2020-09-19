from django.db import models
# Create your models here.
class Users(models.Model):
    car_number=models.IntegerField(max_length=10,unique=True,primary_key=True)
    slot_number = models.IntegerField(max_length=10,unique=True)
     #random.randrange(1,100)
    def __str__(self):
        return f"{self.car_number} - {self.slot_number}"
