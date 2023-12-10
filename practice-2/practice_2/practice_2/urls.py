from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.musician_list, name="musician_list"),
    path("album/", include("album.urls")),
    path("musician/", include("musician.urls")),
]