from django.contrib import admin
import datetime
from django.db.models import Count
# Register your models here.
from apps.portfolio.models import (
    Employment,Projects,
    Technologies, Profile,
)

class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('employer','position', 'location', 'start_date', 'end_date',)
    list_display_links = ('employer',)
    list_filter = ('start_date', )
    empty_value_display = '-empty-' # This attribute overrides the default display value for record’s fields that are empty (None, empty string, etc.). The default value is - (a dash)

    # def projects(self, Employment):
    #     q = Employment.objects.annotate(Count('projects'))
    #     return q.projects__count
    # projects.short_description = 'Number of Projects'

class ProjectADmin(admin.ModelAdmin):
    list_display = ('employment','name', 'description', 'role_responsibility', 'team_size','project_start_date', 'project_endt_date',)
    list_display_links = ('employment','name',)
    search_fields = ('technology__name',)   # many to many search(double under score)
    list_filter = ('start_date',)
    view_on_site = False
    def project_start_date(self, obj):
        return obj.start_date.strftime('%d-%m-%Y')

    def project_endt_date(self, obj):
        return obj.end_date.strftime('%d-%m-%Y')


admin.site.register(Employment, EmploymentAdmin)
admin.site.register(Projects, ProjectADmin)
admin.site.register(Technologies)
admin.site.register(Profile)
