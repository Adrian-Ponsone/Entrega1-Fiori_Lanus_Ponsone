from django.db import models
from datetime import datetime

class User(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    creation_date = models.DateField(null=True)