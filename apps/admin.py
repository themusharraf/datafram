from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apps.models import Material
from apps.app import ReportAdmin


@admin.register(Material)
class MaterialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('material', 'id', 'ulchov')
    list_display = ('id', 'material', 'ulchov', 'miqdori', 'narxi', 'summasi', 'tashkilot')
    fields = ('num', 'material', 'ulchov', 'miqdori', 'narxi', 'summasi', 'tashkilot')
    ordering = ('id',)
    list_filter = ('material', 'ulchov', 'tashkilot')
