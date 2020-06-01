from django.db.models import Q
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.urls import reverse

from .models import Property, Booking

def index(request):
    if request.method == 'POST':
        if 'search_field' in request.POST:
            search_inputs = request.POST['search_field'].replace(',', '').split(' ')
            print(search_inputs)
            for search_input in search_inputs:
                if type(search_input) is 'int':
                    search_part_properties = Property.objects.filter(Q(zip__zip=search_input))
                else:
                    search_part_properties = Property.objects.filter(Q(address__contains=search_input) |
                                                                     Q(zip__city__name=search_input) |
                                                                     Q(zip__city__country__name=search_input))
                print(search_part_properties)
    properties = Property.objects.all()
    context = {
        'properties': properties
    }

    return render(request, "rental/index.html", context)




def single_property(request, pk):
    property_item = Property.objects.get(pk=pk)

    context = {
        'property': property_item
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
