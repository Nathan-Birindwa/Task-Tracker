from django.shortcuts import render
from .models import Task
from django import forms

class add_Item_Form(forms.Form):
    task = forms.CharField(label="Add Task", max_length=100)

List = ["Home", "School"]

# Create your views here.
def index(request):
    if request.method == "post":
        form = add_Item_Form(request.POST)
        if form.is_valid():
            form.cleaned_data["task"]
    
    return render(request, 'main/index.html', {
        "tasks": Task.objects.all(),
        "Input": add_Item_Form(),
        "List": List
    })
