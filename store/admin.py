from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Categorie)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(color)
admin.site.register(size)
admin.site.register(brand)