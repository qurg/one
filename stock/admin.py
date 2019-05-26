from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(IndexList)
class IndexListAdmin(admin.ModelAdmin):
    list_display = ['id', 'index', 'value', 'pe', 'target', 'act', 'create_date', ]


@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', ]
