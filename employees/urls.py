from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeesListView.as_view(), name='employees_list'),
    path('employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_page'),
    path('alphabet/', views.AlphabetPaginatorView.as_view(), name='alphabet'),
    path('filter/', views.EmployeeFilterView.as_view(), name='filter',)
]
