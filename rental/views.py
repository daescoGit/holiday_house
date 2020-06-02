from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.shortcuts import render
from .models import Property, PropertyImg, Booking


def index(request):
    return render(request, 'rental/index.html')


def single_property(request, pk):
    property_item = Property.objects.get(pk=pk)
    property_images = PropertyImg.objects.filter(property=property_item).order_by('order')

    context = {
        'property': property_item,
        'images': property_images
    }

    return render(request, 'rental/property.html', context)


@require_http_methods(["POST"])
def create_booking(request, *args, **kwargs):
    Booking.objects.create(
        customer=request.user,
        property=Property.objects.get(pk=request.POST['property']),
        start_date=request.POST['start_date'],
        end_date=request.POST['end_date']
    )

    return HttpResponseRedirect(reverse('rental:index'))
