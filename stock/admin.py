from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.
# @admin.register(IndexList)
# class IndexListAdmin(admin.ModelAdmin):
#     list_display = ['id', 'index', 'value', 'pe', 'target', 'act', 'create_date', ]


@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', ]


class IndexListResource(resources.ModelResource):
    class Meta:
        model = IndexList
        fields = ('index__name', 'value', 'pe','create_by__username')
        export_order = ('index__name', 'value', 'pe')


@admin.register(IndexList)
class IndexListAdmin(ImportExportModelAdmin):
    resource_class = IndexListResource
    list_display = ['id', 'index', 'value', 'pe', 'target', 'act', 'create_date', ]
