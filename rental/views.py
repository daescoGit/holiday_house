from django.db.models import Q
from django.shortcuts import render
from .models import Property


def index(request):
    if request.method == 'POST':
        if 'search_field' in request.POST:
            search_input = request.POST['search_field']
            print(search_input)
            if type(search_input) is 'int':
                properties = Property.objects.filter(Q(zip__zip=search_input))
            else:
                properties = Property.objects.filter(Q(address__iexact=search_input) |
                                                     Q(zip__city__name__iexact=search_input) |
                                                     Q(zip__city__country__name__iexact=search_input))
            print(properties)
    else:
        properties = Property.objects.all()
    context = {
        'properties': properties
    }

    return render(request, "rental/index.html", context)
