from django.db import models

class Olympics(models.Model):
    id=models.IntegerField(primary_key=True)
    year = models.IntegerField()
    city=models.CharField(max_length=20)
    sport=models.CharField(max_length=20)
    discipline=models.CharField(max_length=30)
    athlete=models.CharField(max_length=50)
    country=models.CharField(max_length=3)
    gender=models.CharField(max_length=5)
    event=models.CharField(max_length=50)
    medal=models.CharField(max_length=10)