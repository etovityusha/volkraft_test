from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django_filters.views import FilterView

from .models import Employee
from .services.pagination_alphabetically import NamePaginator
from .filters import EmployeeFilter


class EmployeesListView(ListView):
    template_name = 'employees/employee_list.html'
    paginate_by = 25
    model = Employee

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context.get('paginator')
        num_pages = paginator.num_pages
        current_page = context.get('page_obj')
        page_no = current_page.number
        if num_pages <= 11 or page_no <= 6:
            pages = [x for x in range(1, min(num_pages + 1, 12))]
        elif page_no > num_pages - 6:
            pages = [x for x in range(num_pages - 10, num_pages + 1)]
        else:
            pages = [x for x in range(page_no - 5, page_no + 6)]
        context.update({'pages': pages})
        return context


class EmployeeDetailView(DetailView):
    model = Employee


class EmployeeFilterView(FilterView):
    template_name = 'employees/employee_filtration.html'
    model = Employee
    filter_class = EmployeeFilter
    filterset_fields = {
            'work_start_date': ['lt', 'gt'],
            'department': ['exact'],
        }


class AlphabetPaginatorView(ListView):
    template_name = 'employees/alphabet_selectors.html'
    model = Employee

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = NamePaginator(Employee.objects.all(), on="last_name", per_page=len(Employee.objects.all()) // 6)
        try:
            page = int(self.request.GET.get('page', '1'))
        except ValueError:
            page = 1
        try:
            page = paginator.page(page)
        except:
            page = paginator.page(paginator.num_pages)
        context['page'] = page
        context["paginator_pages"] = paginator.pages
        return context
