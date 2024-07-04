from django.shortcuts import render, redirect
from . import forms


# Create your views here.
def Task(request):
    if request.method == "POST":
        taskForm = forms.TaskForm(request.POST)
        if taskForm.is_valid():
            taskForm.save()
            return redirect("homepage")
    else:
        taskForm = forms.TaskForm()
    return render(request, "addTask.html", {"form": taskForm})
