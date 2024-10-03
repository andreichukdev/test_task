# Team and People Management API

Цей проєкт є Django REST API для управління командами та людьми. Проєкт використовує `Django REST Framework` для реалізації CRUD операцій для команд та людей.

## Вимоги

- Python 3.12+
- pipenv (для управління залежностями)
- Postman (для тестування API)

## Встановлення

### 1. Клонування репозиторію та налаштування проєкту

Спочатку клонуй репозиторій, перейди до директорії проєкту, встанови всі залежності та активуй віртуальне середовище:

```bash
git clone https://github.com/andreichukdev/test_task.git
cd your-repo
```


### 2. Встановлення залежностей
```bash
pipenv install
pipenv shell
```

### 3. Запуск
```bash
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

### 3. Тестування API в Postman

Тестуй API через Postman, використовуючи наступні маршрути:

Команди

	1.	Отримати список команд: GET /api/teams/
	2.	Створити нову команду: POST /api/teams/
	•	Приклад тіла запиту:
    {
        "name": "Team Alpha"
    }

    3.	Отримати конкретну команду: GET /api/teams/<id>/
	4.	Оновити команду: PUT /api/teams/<id>/
	5.	Видалити команду: DELETE /api/teams/<id>/

Люди

	1.	Отримати список людей: GET /api/people/
	2.	Створити нову людину: POST /api/people/
	•	Приклад тіла запиту:
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "team": 1
    }