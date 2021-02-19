from django.test import TestCase
from .models import Employee, Department, Position


class AlphabetPaginatorTest1(TestCase):
    def setUp(self):
        Position.objects.create(position_title='Программист')
        Department.objects.create(department_title='Разработка')

        for last_name in ['Аа', 'Вв', 'Гг', 'Ее', 'Жж', 'Кк', 'Лл', 'Фф', 'Чч', 'Ъъ', 'Юю', 'Яя']:
            Employee.objects.create(
                first_name='Александр',
                last_name=last_name,
                patronymic='Иванович',
                birth_date='1999-12-31',
                email='none@none.com',
                phone='89161234567',
                work_start_date='2020-01-01',
                position=Position.objects.get(position_title='Программист'),
                department=Department.objects.get(department_title='Разработка'),
            )

    def test_response(self):
        response = self.client.get('/alphabet/')
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        response = self.client.get('/alphabet/')
        self.assertEqual(
            list(map(str, response.context['paginator_pages'])),
            ['А-В', 'Г-Е', 'Ж-К', 'Л-Ц', 'Ч-Э', 'Ю-Я']
        )
        self.assertEqual(response.context['page'], response.context['paginator_pages'][0])
        self.assertLessEqual(len(response.context['paginator_pages']), 7)
