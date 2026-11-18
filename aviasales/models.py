from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Airlines(models.Model):
    airline_name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.airline_name
    

class Airport(models.Model):
    airport_name = models.CharField(max_length=150) 
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)

    def __str__(self):
        return self.airport_name
    

class Tickets(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airlines, on_delete=models.CASCADE)
    departure = models.CharField(max_length=150)
    arrival = models.CharField(max_length=150)
    flight = models.DateField(default=datetime.now)
    landing = models.DateField(default=datetime.now)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.departure} - {self.arrival}"