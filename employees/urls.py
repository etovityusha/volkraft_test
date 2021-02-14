from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeesListView.as_view(), name='employees_list'),
    path('department/<int:pk>/', views.DepartmentEmployeesList.as_view(), name='employees_by_department'),
    path('employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_page'),
]
