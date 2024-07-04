from django import forms
from .models import Task_Model


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task_Model
        fields = "__all__"
