from django.contrib import admin
from .models import *
# Register your models here.
class UserDataAdmin(admin.ModelAdmin):
  list_display=('id','name','email','password')

admin.site.register(UserData,UserDataAdmin)