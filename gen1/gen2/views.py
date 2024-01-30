from django.shortcuts import render
from .models import *
import os
from datetime import datetime
from ipware import get_client_ip
from geopy.geocoders import Nominatim
from gen1.settings import MEDIA_ROOT
# Create your views here.
userid=''
userid2=''
user=False
def index(request):
  global user
  print(user)
  return render(request,'first.html',{'user':user,'message':'none'})

def login(request):
        global userid,user,userid2
        name=request.POST['user']
        passw=request.POST['password']
        usern=UserData.objects.filter(email=name).values()
        print(usern)
        if(usern.exists()):
                if usern[0]['password']==passw:
                     userid=name
                     userid2=usern[0]['name']
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
               return login(request)
        
def music(request):
       return render(request,'music.html')

def events(request):
       return render(request,'events.html')

def community(request):
       posts1=posts.objects.all()
       print(posts1)
       return render(request,'community.html',{'posts':posts1,"user":user,"userid":userid2})

USER_AGENT='gen1/1.0'
def posting(request):
   try: 
        global userid, userid2
        desc = request.POST['desc']
        p=request.FILES.get('file').name
        client_ip, is_routable = get_client_ip(request)
        place_name="UNKNOWN_PLACE"
        if client_ip and is_routable:
                geolocator = Nominatim(user_agent=USER_AGENT)
                location = geolocator.reverse(client_ip)

                if location:
                        place_name = location.address
        current_time = datetime.now().time()
        formatted_time = current_time.strftime('%H:%M:%S')
        npost = posts(uploaderemail=userid, uploader=userid2, desc=desc, time=formatted_time, location=place_name,file = request.FILES.get('file'))
        image_path = os.path.join(MEDIA_ROOT, p)
        print(image_path)
        print(os.path.exists(image_path))
        npost.save()
        posts1=posts.objects.all()
        print(posts1)
        return render(request,'community.html',{'posts':posts1,"user":user,"userid":userid2})
   except Exception as e:
                print(e)
                data = posts.objects.filter(name=userid).values()

                return render(request, 'community.html', {'posts': data,"user":user})
def quiz(request):
       return render(request,'quiz.html')

def experiance(request):
       return render(request,'experiances.html')