from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
import random 

# Create your views here.
def sayhello(request):
    return HttpResponse("Hello Django!")

def hello2(request, username):
    return HttpResponse("Hello "  + username)

def hello3(request, username):
    now = datetime.now()
    return render(request, "hello3.html",locals())

def hello4(request, username):
    now = datetime.now()
    return render(request, "hello4.html",locals())

def dice(request):
    no1 = random.randint(1, 6)
    no2 = random.randint(1, 6)
    no3 = random.randint(1, 6)
    return render(request, "dice.html", locals())

def show(request):
    p1 = {"name" : "Amy", "phone": "049-1234657", "age": 20}
    p2 = {"name" : "Jack", "phone": "02-4455666", "age": 25}
    p3 = {"name": "Nacy", "phone": "04-9876543", "age": 17}
    person = [p1, p2, p3]
    return render(request, "show.html", locals())

def djget(request):
    name = request.GET['name']
    city = request.GET['city']
    return render(request, "djget.html", locals())

def djpost(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username == "david" and password == "1234":
            return HttpResponse("歡迎光臨本網站! ")
        else:
            return HttpResponse("帳密或密碼有誤! ")
    else:
        return render(request, "djpost.html", locals())
