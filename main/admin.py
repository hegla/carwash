from django.contrib import admin


from .models import Carwash, Order, Customer


admin.site.register(Carwash)
admin.site.register(Order)
admin.site.register(Customer)
