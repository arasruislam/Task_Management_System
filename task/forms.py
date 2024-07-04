from django import forms
from .models import Task_Model


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task_Model
        fields = [
            "title",
            "description",
            "is_completed",
            "Task_Assign_Data",
            "category",
        ]

        widgets = {
            "Task_Assign_Data": forms.DateInput(attrs={"type": "date"}),
            "category": forms.CheckboxSelectMultiple,
        }
