from django.shortcuts import render
from django import forms

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

def sign_up(request):
    return render(request, "Auth/Sign_up.html")

def Login(request):
    return render(request, "Auth/Login.html")