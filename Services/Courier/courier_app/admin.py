from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import Courier, Order


class CustomUserAdmin(UserAdmin):
    model = Courier
    list_display = ['username', 'first_name','last_name', 'status']


admin.site.register(Courier, CustomUserAdmin)
admin.site.register(Order)

admin.site.site_header = 'Администрирование курьеров'

