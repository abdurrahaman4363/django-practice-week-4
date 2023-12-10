from django.db import models
from category.models import Category

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    assigned_date = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title