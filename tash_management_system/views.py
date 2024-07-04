from django.shortcuts import render
from task.models import Task_Model


def home(request):
    tasks = Task_Model.objects.all()
    return render(request, "index.html", {"tasks": tasks})
