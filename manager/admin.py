from django.contrib import admin

from .models import Employee, Cart, Order, Marketing, MarketingEmail

admin.site.register(Employee)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Marketing)
admin.site.register(MarketingEmail)
