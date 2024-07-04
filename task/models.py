from django.db import models
from category.models import CategoryModel


# Create your models here.
class Task_Model(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    is_completed = models.BooleanField()
    Task_Assign_Data = models.DateField()

    # relation with category => many to many relation
    category = models.ManyToManyField(CategoryModel)

    def __str__(self) -> str:
        return self.title
