from django.db import models

# Create your models here.
class UserData(models.Model):
  name=models.CharField(max_length=2080)
  email=models.EmailField(unique=True,primary_key=True)
  password=models.CharField(max_length=2080)