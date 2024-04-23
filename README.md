# Ref_system
>Реферальная система

Стек:Django, DRF, postgreSQL

#### Как запустить проект:

+ клонируем репозиторий `git clone`
`git@github.com:BeerBellyWell/ref_system.git`
+ переходим в него `cd ref_system/`
    + разворачиваем виртуальное окружение
    `python3 -m venv env` (Windows: `python -m venv env`)
    + активируем его
    `source env/bin/activate` (Windows: `source env/scripts/activate`)
    + устанавливаем зависимости из файла requirements.txt
    `pip install -r requirements.txt`
+ выполняем миграции
`python3 manage.py migrate` (Windows: `python manage.py migrate`)
+ запускаем проект
`python3 manage.py runserver` (Windows: `python manage.py runserver)

# Env-файл создать в корне:
+ DB_ENGINE=django.db.backends.postgresql # работаем с БД postgresql
+ DB_NAME=""ВАШЕ ИМЯ БД # имя базы данных
+ POSTGRES_USER="ВАШЕ ИМЯ ПОЛЬЗОВАТЕЛЯ" # логин для подключения к базе данных
+ POSTGRES_PASSWORD="ВАШ ПАРОЛЬ" # пароль для подключения к БД
+ DB_HOST=localhost
+ DB_PORT=5432 # порт для подключения к БД

# Инструкции и примеры

>Основные эндпойнты `/api/v1/`:

/user/ - get запрос, получить список всех пользователей.
- response: [
    {
        "id": 2,
        "phone_number": 12345,
        "invite_code": "57SD4B",
        "someone_invite_code": null,
        "invited_users": []
    }
]

/user/2/ - get запрос, получить отдельного пользователя
- response: {
        "id": 2,
        "phone_number": 12345,
        "invite_code": "57SD4B",
        "someone_invite_code": null,
        "invited_users": [1234567890]
    }

/user/ - post запрос, создать пользователя
- request: {
    "phone_number": 1234567890,
    "someone_invite_code": "57SD4B"  # Опционально
}
- response: {
    "id": 3,
    "phone_number": 123456789,
    "invite_code": "Q36FZ1",
    "someone_invite_code": "57SD4B",
    "invited_users": []
}

/user/2/ - patch запрос, установить поле someone_invite_code, если оно не задано
- request: {
    "someone_invite_code": "57SD4B"
}
- response: {
    "id": 3,
    "phone_number": "1234567890",
    "invite_code": "Q36FZ1",
    "someone_invite_code": "57SD4B",
    "invited_users": []
}





