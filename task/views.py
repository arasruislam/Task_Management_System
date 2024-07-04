from django.shortcuts import render, redirect
from . import forms, models


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


def EditTask(request, id):
    task = models.Task_Model.objects.get(pk=id)

    taskForm = forms.TaskForm(instance=task)
    if request.method == "POST":
        taskForm = forms.TaskForm(request.POST, instance=task)
        if taskForm.is_valid():
            taskForm.save()
            return redirect("homepage")

    return render(request, "addTask.html", {"form": taskForm})


def DeleteTask(request, id):
    task = models.Task_Model.objects.get(pk=id)
    task.delete()
    return redirect("homepage")
