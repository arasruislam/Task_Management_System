from django.urls import path
from . import views

urlpatterns = [
    path("task/", views.Task, name="task"),
    path("edit/<int:id>", views.EditTask, name="EditTask"),
    path("delete/<int:id>", views.DeleteTask, name="DeleteTask"),
]
