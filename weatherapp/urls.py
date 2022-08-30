from django.urls import path
from . import views

#calling the index function in the views.py file

urlpatterns = [
    path('', views.index),
]
