from django.db import models
from datetime import datetime

class Members(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  fecha = models.DateField(default=datetime.today)
