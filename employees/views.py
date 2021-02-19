from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django_filters.views import FilterView

from .models import Employee
from .services.pagination_alphabetically import NamePaginator
from .services.pages_list_for_paginator import get_pages_list_for_paginator
from .filters import EmployeeFilter

import math


class EmployeesListView(FilterView, ListView):
    model = Employee
    filterset_class = EmployeeFilter
    template_name = 'employees/employee_list.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = get_pages_list_for_paginator(context=context)
        return context


class EmployeeDetailView(DetailView):
    model = Employee


class AlphabetPaginatorView(ListView):
    template_name = 'employees/alphabet_selectors.html'
    model = Employee

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        objects = Employee.objects.all()
        paginator = NamePaginator(objects, on='last_name', per_page=math.ceil(len(objects)/7))
        try:
            page = int(self.request.GET.get('page', '1'))
        except ValueError:
            page = 1
        try:
            page = paginator.page(page)
        except:
            page = paginator.page(paginator.num_pages)
        context['page'] = page
        context['paginator_pages'] = paginator.pages
        return context
