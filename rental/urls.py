from . import views
from django.urls import path


app_name = 'rental'

urlpatterns = [
    path('', views.index, name="index"),
]
