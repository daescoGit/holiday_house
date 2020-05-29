from django.contrib import admin

from django.contrib import admin
from .models import Role, UserProfile, Country, City, Booking, Property, Zip, PropertyImg

admin.site.register(Country)
admin.site.register(UserProfile)
admin.site.register(Role)
admin.site.register(City)
admin.site.register(Booking)
admin.site.register(Property)
admin.site.register(Zip)
admin.site.register(PropertyImg)
