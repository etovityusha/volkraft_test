from django.contrib import admin
from employees.models import Employee, Department, Position


class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Employee._meta.fields]
    list_filter = ('department', 'work_start_date',)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_title', )


class PositionAdmin(admin.ModelAdmin):
    list_display = ('position_title', )


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Position, PositionAdmin)
