from django.db import models
from datetime import datetime

class Members(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  fecha = models.DateField(default=datetime.today)
  
  def __str__(self):
    return f"{self.firstname},{self.lastname},{self.fecha}"

