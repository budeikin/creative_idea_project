from django.db import models


# Create your models here.

class Silo(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    current_stock = models.PositiveIntegerField()


class SiloLog(models.Model):
    silo = models.ForeignKey(Silo, on_delete=models.CASCADE, related_name='logs')
    change_type = models.CharField(max_length=100)
    amount = models.PositiveIntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)
