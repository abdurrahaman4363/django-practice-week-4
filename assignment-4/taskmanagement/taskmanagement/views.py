from django.shortcuts import render
from task.models import Task


def show_task(request):
    data = Task.objects.all()
    return render(request, "show.html", {"data": data})