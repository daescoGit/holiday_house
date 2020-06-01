from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('property/<int:pk>', views.single_property, name='property'),
]
