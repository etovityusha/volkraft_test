from django.db import models
from django.urls import reverse


class Position(models.Model):
    position_title = models.CharField(max_length=100, verbose_name='Должность')

    def __str__(self):
        return self.position_title

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Department(models.Model):
    department_title = models.CharField(max_length=100, verbose_name='Отдел')

    def __str__(self):
        return self.department_title

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Employee(models.Model):
    first_name = models.CharField(max_length=55, verbose_name='Имя')
    last_name = models.CharField(max_length=55, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=55, verbose_name='Отчество')
    birth_date = models.DateField(verbose_name='Дата рождения')
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')
    work_start_date = models.DateField(verbose_name='Дата начала работы')
    work_end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания работы')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Должность')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Отдел')

    def get_absolute_url(self):
        return reverse('employee_page', args=[str(self.pk)])

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
        ordering = ['pk']
