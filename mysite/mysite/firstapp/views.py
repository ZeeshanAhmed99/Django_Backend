from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import formdata
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from .serializers import getdataSerializer
from .models import getdata
import pymysql


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def data(request):
    def send(request):
        return render(request, 'index.html')
    if request.method == 'POST':
        Name = request.POST.get("UserName")
        Email = request.POST.get("Email")
        Password = request.POST.get("Password")
        s = formdata(Name=Name, Email=Email, Password=Password)
        s.save()
        params = {'Msg':'Registered Successfully'}
    else:
        params = {'Msg':''}
    return render(request,'index.html',params)




def login(request):
    def credentials(request):
        return render(request, 'login.html')
    Email = request.POST.get("Email")
    Password = request.POST.get("Password")
    auth = formdata.objects.filter(Email=Email, Password=Password)
    if(auth):
        params = {'Msg': 'Login Successful'}
        print('PASS')   
    else:
        params = {'Msg': ''}
        print('FAILED')
    return render(request,'login.html',params)   

def temp(request):
    context = {'mylist':[5,4,3,2,1],'text':'You have done it'}
    return render(request,'Home.html',context)
        
def database(request):
    auth = formdata.objects.get(id = 2)
    context = {'data': auth.Password}
    return render(request,'data.html',context)


def removepunc(request):
    new = ""
    if request.method== "POST":
        msg = request.POST.get("text")
        punc = ".,;:?$^!'-()[]''/@&{ }#%"
        for i in range(0,len(msg)):
            if msg[i] not in punc:
                new = new + msg[i]
            else:
                print(msg[i])
        context = {'text':new}
    else:
        context = {'text':''}
    return render(request,'text.html',context)   

def capital(request):
    if request.method== "POST":
        msg = request.POST.get("text")
        msg=msg.swapcase()
        context = {"msg":msg}
    else:
        context = {'msg': ''}
    return render(request,'text.html',context)    


class getdataViewSet(viewsets.ModelViewSet):
    queryset = getdata.objects.all().order_by('id')
    serializer_class = getdataSerializer



# Create your views here.
