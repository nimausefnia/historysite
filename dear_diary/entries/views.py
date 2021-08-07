from entries.forms import EntryForm
from django.forms.models import ModelForm
from entries.models import Entry
from django.shortcuts import render,redirect

def index(request):


    entries=Entry.objects.order_by('-date_posted')

    context={'entries': entries}


    return render(request,'entries/index.html',context)






def add(request):
    
    if request.method=="POST":
         form=EntryForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect("index")
    else:
         form=EntryForm()
    context={'form':form}
    
    return render(request,'entries/add.html',context)
