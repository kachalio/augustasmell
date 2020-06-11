from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from datetime import datetime
from smell.forms import UpdateSmell
from smell.models import Smell


# Create your views here.

def index(request):
    smells = Smell.objects.order_by('-pk')
    num_smells = len(smells)
    if num_smells > 0:
        smell_current = smells[0]
        if num_smells > 1:
            max_smells = 6 if num_smells > 6 else num_smells
            smell_history = smells[1:max_smells]
            return render(request, 'smell/smell.html', {'smell_current' : smell_current, 'smell_history' : smell_history})
        else:
            return render(request, 'smell/smell.html', {'smell_current' : smell_current})
    return render(request, "smell/smell.html")

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

