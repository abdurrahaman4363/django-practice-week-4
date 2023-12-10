
from django.urls import path
# from first_app.views import about, home
from . import views

urlpatterns = [
    path('',views.home, name = 'homepage'),
    path('about/',views.about, name = 'aboutpage'),
    path('form/',views.form, name = 'form'),
    path('djangoForm/',views.djangoForm, name = 'djangoForm'),
]
