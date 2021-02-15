import django_filters
from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = {
            'work_start_date': ['lt', 'gt'],
            'department': ['exact'],
        }
