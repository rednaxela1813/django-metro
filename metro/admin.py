from django.contrib import admin
from .models import Category, Product, Supliers, Factura, Phone, Email
from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)


@admin.register(Supliers)
class SupliersAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)




