from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    date = datetime.now()
    smell = "The South"
    return render(request, 'smell/smell.html', {'date' : date, 'smell' : smell})
