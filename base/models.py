from statistics import mode
from turtle import update
import uuid
from venv import create
from django.db import models

# Create your models here.
class Item(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, null=False)
    name = models.CharField(max_length=200)
    desciption = models.CharField(max_length=255, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)