from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Student(models.Model):
  name = models.CharField(max_length=64)
  birth_date = models.DateField()
  major = models.CharField(max_length=64)
  graduation_date = models.DateField()
  admitted_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

  def __str__(self):
    return self.name

