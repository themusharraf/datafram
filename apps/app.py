from import_export import resources
from apps.models import Material
from import_export.admin import ImportExportModelAdmin


class ReportResource(resources.ModelResource):
    class Meta:
        model = Material


class ReportAdmin(ImportExportModelAdmin):
    resource_class = ReportResource
