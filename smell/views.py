from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from datetime import datetime
from smell.forms import UpdateSmell
from smell.models import Smell


# Create your views here.

def index(request):
    date = datetime.now()
    smell = "Rain"
    # next line gets the most recent entry to display
    current_smell = Smell.objects.order_by('-pk')[0]
    last_five_smells = Smell.objects.order_by('-pk')[1:6]
    return render(request, 'smell/smell.html', {'date' : current_smell.updated_datetime, 'smell' : current_smell.smell, 'smell_history' : last_five_smells})

def update(request):
    if request.method == "POST":
        form = UpdateSmell(request.POST)
        # print(form)
        if form.is_valid():
            new_smell = form.save(commit=False)
            new_smell.updated_datetime = datetime.now()
            print(form)
            new_smell.save()
            return redirect(reverse('index'))
    else:
        form = UpdateSmell()
    return render(request, 'smell/update.html',{'form':form})

