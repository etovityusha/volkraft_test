### Веб приложение для хранения данных о сотрудниках.

Для установки необходимо:
- Cклонировать репозиторий: 
  
        git clone URL_repository
  
- Cоздать виртуальное окружение:
  
        python3 -m venv venv
  
- Активировать окружение. 
  
        source venv/bin/activate

- Установить зависимости: 
  
        pip3 install -r requirements


    Опционально:
    - Изменить в volkraft/.env соединение с базой данных
    - Зарегистрировать супер-пользователя Django: python3 manage.py createsuperuser
    - Создать миграции для БД: python3 manage.py makemigrations
    - Импортировать миграции в БД: python3 manage.py migrate

- Запустить Django сервер: 
  
        python3 manage.py runserver