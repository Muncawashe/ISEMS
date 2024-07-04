from django.contrib import admin
from .models import  Role, Department, User

from import_export.admin import ImportExportModelAdmin

class UserAdmin(ImportExportModelAdmin):
    list_display = ['first_name', 'email']

class DepartmentAdmin(ImportExportModelAdmin):
    list_display = ['name']

class RoleAdmin(ImportExportModelAdmin):
    list_display = ['name']

admin.site.register(User, UserAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Department, DepartmentAdmin)



