from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import Courier

admin.site.register(Courier, UserAdmin)
