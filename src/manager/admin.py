from django.contrib import admin

from .models import Employee, Cart, Order

admin.site.register(Employee)
admin.site.register(Cart)
admin.site.register(Order)
