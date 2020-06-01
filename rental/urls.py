from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'rental'

urlpatterns = [
    path('', views.index, name='index'),
    path('property/<int:pk>', views.single_property, name='property'),
    path('booking/create', views.create_booking, name='booking_create'),
]
