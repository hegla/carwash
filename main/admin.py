from django.contrib import admin
from mapbox_location_field.admin import MapAdmin

from .models import Carwash, Order, Customer


admin.site.register(Carwash, MapAdmin)
admin.site.register(Order)
admin.site.register(Customer)
