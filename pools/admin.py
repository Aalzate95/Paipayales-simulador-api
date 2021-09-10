from django.contrib import admin
from .models import *


@admin.register(Pools)
class PoolsAdmin(admin.ModelAdmin):
    list_display = ('name','size','pool_type')