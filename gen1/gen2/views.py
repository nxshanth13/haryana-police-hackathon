from django.shortcuts import render
from .models import *
# Create your views here.
userid=''
def index(request):
  return render(request,'first.html')

def logins(request):
        global userid
        print(userid)
        n2=UserData.objects.filter(id=int(userid)).values()
        c=[]
        pro=list(set(map(int,n2[0]['products'].split(','))))
        pro.sort(reverse=True)
        for i in pro:
                g=Content.objects.filter(id=i).values()
                c.append(g)
        return render(request,'login.html',{'n2':n2[0],'pros':c})