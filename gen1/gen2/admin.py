from django.contrib import admin
from .models import *
# Register your models here.
class UserDataAdmin(admin.ModelAdmin):
  list_display=('name','email','password')
class postsAdmin(admin.ModelAdmin):
  list_display=('uploader','location','time','file','desc','comments')
admin.site.register(UserData,UserDataAdmin)
admin.site.register(posts,postsAdmin)