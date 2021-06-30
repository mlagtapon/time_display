from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    return redirect("/time_display")

def time(request):
    context = {
        "date": strftime("%B %d, %Y", gmtime()),
        "time": strftime("%H:%M %p", gmtime())
    }
    return render(request,'index.html', context)