from django.db import models

# Create your models here.
class UserData(models.Model):
  id=models.CharField(max_length=2080,unique=True,primary_key=True)
  name=models.CharField(max_length=2080)
  email=models.EmailField()
  password=models.CharField(max_length=2080)