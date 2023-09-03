from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apps.models import Material
from apps.app import ReportAdmin


@admin.register(Material)
class MaterialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('material', 'id','ulchov_briligi')
    list_display = ('id', 'material', 'ulchov_briligi', 'miqdori', 'narxi', 'summasi')
    fields = ('material', 'ulchov_briligi', 'miqdori', 'narxi', 'summasi')
    ordering = ('id',)
    list_filter = ('material', 'ulchov_briligi', 'miqdori', 'narxi', 'summasi')
