from django.shortcuts import render
from musician.models import Musician
from album.models import Album


def musician_list(request):
    musicians = Musician.objects.all()
    return render(request, "musician_list.html", {"musicians": musicians})