from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import Order, Position, Client


class PositionInline(admin.TabularInline):
    model = Position


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        PositionInline
    ]


admin.site.register(Client, UserAdmin)
admin.site.register(Order, OrderAdmin)
