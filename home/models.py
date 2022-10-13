from django.db import models
from datetime import datetime

class User(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    registration_date = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.name} {self.last_name}'