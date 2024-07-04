from django.shortcuts import render


# Create your views here.
def Task(request):
    return render(request, "addTask.html")
