from django.shortcuts import render
from .models import Task
from django import forms

class add_Item_Form(forms.Form):
    task = forms.CharField(label="Add Task", max_length=100)

List = [{
    "id": 1,
    "name": "Go to gym",
    "dec": "Go and burn out some fats to not end like you know"},
    {
    "id": 1,
    "name": "Go to Town",
    "dec": "Go and burn out some fats to not end like you know"},
    {
    "id": 1,
    "name": "Go to Town",
    "dec": "Go and burn out some fats to not end like you know"},

        ]

# Create your views here.
def index(request):
   
    
    return render(request, 'main/index.html', {
        "tasks": Task.objects.all(),
        "Input": add_Item_Form(),
        "List": List
    })
def add(request):
    return render(request, 'Task/add.html')