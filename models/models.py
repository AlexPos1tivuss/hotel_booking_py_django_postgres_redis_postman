from django.db import models
from rest_framework.authtoken.admin import User


class Room(models.Model):
    number = models.IntegerField()
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class UserBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=50)

class User(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
