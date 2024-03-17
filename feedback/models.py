from django.db import models

class Feedback(models.Model):
    food_rating = models.CharField(max_length=20)
    recommendation = models.IntegerField()
    name = models.CharField(max_length=100, blank=True)
    mobile_number = models.CharField(max_length=15, blank=True)
