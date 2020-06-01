from django.db.models import Q
from django.shortcuts import render
from .models import Property

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
