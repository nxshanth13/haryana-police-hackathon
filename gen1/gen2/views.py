from django.shortcuts import render
from .models import *
# Create your views here.
userid=''
user=False
def index(request):
  return render(request,'first.html',{'user':user,'message':'none'})

def login(request):
        global userid,user
        name=request.POST['user']
        passw=request.POST['password']
        usern=UserData.objects.filter(email=name).values()
        print(usern)
        if(usern.exists()):
                if usern[0]['password']==passw:
                     userid=name
                     user=True
                     return render(request,'first.html',{'user':user})
                else:
                        return render(request,'first.html',{'error_message':"password error",'user':user})
        else:
               return render(request,'first.html',{'error_message':'user does not exist','user':user})
       
def register(request):
        try:
                global user
                name=request.POST["name"]
                email=request.POST['email']
                passw=request.POST['password']
                repassw=request.POST['repassword']
                user=UserData.objects.filter(email=email)
                print(name,email,passw,repassw)
                if(user.exists()):
                        print("yes1")
                        return render(request,'first.html',{"error_message":"email already exists",'user':user})
                else:
                        print('yes2')
                        if(passw!='' and passw==repassw):
                                usern=UserData(name=name,email=email,password=passw)
                                usern.save()
                                return render(request,'first.html',{"user":user})
                        else:
                                return render(request,'first.html',{'user':user,'error_message':'Paaword error'})
        except:
               return render(request,'first.html',{'user':user})
        
def music(request):
       return render(request,'music.html')

def events(request):
       return render(request,'events.html')