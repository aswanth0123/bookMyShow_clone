from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import *


# Login page
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            request.session['user']=username
            auth.login(request,user)
            return redirect(index)
        else :
            return redirect(login)
    else:
        return render(request,'login.html')
    

def logout1(request):
        auth.logout(request)
        print(request.user)

        return redirect(index)

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        data=User.objects.create_user(username=username,email=email,password=password)
        data.save()
        return redirect(login)
    else:
        return render(request,'register.html')
    

# pages
def index(request):
    movie1=movie.objects.all()[0:8]
    return render(request,'index.html',{'movie':movie1})

def see_all(request,lang=None):
    movie1=[]
    if lang:
        l=language.objects.filter(language=lang)
        movie1=[i.movie_name for i in l]
    else:
        movie1=movie.objects.all()
    lang2={i.language for i in language.objects.all()}
    return render(request,'see_all.html',{'movie':movie1,'lang':lang,'lang2':lang2})

def view_movie(request,name):
    movie1=movie.objects.get(name=name)
    lang=language.objects.filter(movie_name=movie1)
    data=movie_members.objects.filter(movie_name=movie1)
    cast=[i for i in data if i.member_name.type=='cast']
    crew=[i for i in data if i.member_name.type!='cast']
    movies=movie.objects.all()
    return render(request,'movie.html',{'movie':movie1,'lang':lang,'cast':cast,'crew':crew,'movies':movies})

def view_theatre(request,name):
    movie1=movie.objects.get(name=name)
    lang=language.objects.filter(movie_name=movie1)[:1]
    
    show=Show.objects.filter(movie=movie1)
    theater_names={i.screen.theater.name for i in show }
    return render(request,'select_theatre.html',{'movie':movie1,'lang':lang,'shows':show,'theater_names':theater_names})

def select_seat(req,pk):
    seat=Show.objects.get(pk=pk)
    return render(req,'select_seat.html',{'dtls':seat}) 