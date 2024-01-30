from django.db import models

# Create your models here.
class UserData(models.Model):
  name=models.CharField(max_length=2080)
  email=models.EmailField(unique=True,primary_key=True)
  password=models.CharField(max_length=2080)

class posts(models.Model):
  uploaderemail=models.EmailField(default="abc@gmail.com")
  uploader=models.CharField(max_length=2080)
  location=models.CharField(max_length=2080)
  time=models.TimeField()
  file=models.ImageField(upload_to='photos')
  desc=models.TextField()
  comments=models.TextField()