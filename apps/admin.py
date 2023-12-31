from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apps.models import Material


@admin.register(Material)
class MaterialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('material', 'id', 'ulchov')
    list_display = ('id', 'cod', 'material', 'ulchov', 'miqdori', 'narxi', 'summasi', 'tashkilot')
    fields = ('material', 'cod', 'ulchov', 'miqdori', 'narxi', 'summasi', 'tashkilot')
    ordering = ('id',)
    list_filter = ('material', 'tashkilot')
