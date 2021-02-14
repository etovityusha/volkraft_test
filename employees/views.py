from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404, render
from django.db.models.functions import Substr

from employees.models import Employee, Department


class EmployeesListView(ListView):
    paginate_by = 10
    model = Employee

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        return context


class EmployeeDetailView(DetailView):
    model = Employee

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        return context


class DepartmentEmployeesList(ListView):
    template_name = 'employees/employees_by_department.html'
    context_object_name = 'employees'
    paginate_by = 10

    def get_queryset(self):
        self.department = get_object_or_404(Department, pk=self.kwargs['pk'])
        return Employee.objects.filter(department=self.department)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        context['department'] = self.department
        return context
