from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>HELLO WORLD</h1>')

def home(request):
    return render(request,"index.html",{'active': 'home'})

def contact(request):
    return render(request,"contact.html",{'active': 'contact'})

def log(request):
    return render(request,"log.html",{'active': 'log'})

def help(request):
    return render(request,"help.html",{'active': 'about'})

def homepage(request):
    return render(request, 'index.html', {'active': 'home'})