from django.db import models


# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=25, help_text="enter your category name")

    def __str__(self) -> str:
        return self.name
