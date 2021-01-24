from django.shortcuts import render, redirect
import pyttsx3

# Create your views here.


def home(request):
    return render(request, '_base.html',context={})


def textInput(request):
    value=request.GET['int'] 
    obj = pyttsx3.init()
    obj.say(value)
    obj.runAndWait()
    return redirect('/')
