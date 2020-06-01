from django.http import HttpResponse
from django.shortcuts import render
from .models import Property

# Create your views here.


def single_property(request, pk):
    property_item = Property.objects.get(pk=pk)

    context = {
        'property': property_item
    }

    return render(request, 'rental/property.html', context)
