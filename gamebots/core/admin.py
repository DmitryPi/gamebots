from django.contrib import admin

from .models import LicenseKey, Order, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(LicenseKey)
class LicenseKeyAdmin(admin.ModelAdmin):
    pass
