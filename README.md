# goodd_test_api
API сервис. Можно создавать задачи, редактировать их. Авторизация по jwt токену. Доступ на редактирование есть только к своим задачам. Get запрос показывает только задачи, созданные данным пользователем. База PostgreSQL, полный список задач кешируется через Redis. Количество запросов ограничено до 100 в минуту.
### Как запустить проект:

Клонировать репозиторий (дефолт ветка master):

```
git clone https://github.com/FFFSanchez/goodd_test_api.git
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Настроить подключение к базе Postgre в settings.py:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '***',
        'USER': ''***',',
        'PASSWORD': ''***',',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

Настроить запустить Redis и проверить его адрес:

```
sudo apt-get install redis
sudo service redis-server start
redis-cli 
127.0.0.1:6379> ping
PONG
```

Настроить Redis в settings.py:

```
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379',
    }
}

```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
### Примеры использования:

1) Регистрация нового пользователя:
* Отправить POST-запрос http://127.0.0.1:8000/api/v1/register/. В теле запроса указать: 
```
{
    "username": "string",
    "password": "string",
    "email": "ex@ex.ru"
}
```

2) Получение JWT-токена:
* Отправить POST-запрос http://127.0.0.1:8000/api/v1/login/. В теле запроса указать:
```
{
    "username": "string",
    "password": "string"
}
```
* В ответ придёт JWT-токен в форме:

```
{
    "access": "string",
    "refresh": "string"
}
```
* access токен нужно вставлять в заголовок запроса в формате:

```
Token ey3t1.....
```

* С валидным токеном юзер считается авторизованным, время жизни можно изменять в settings.py
* По истечению access токена нужно отправить ПОСТ запрос на http://127.0.0.1:8000/api/v1/refresh/
```
{
    "refresh": "string"
}
```


3) Чтобы разлогиниться, то есть в случае с jwt добавить рефреш токен в блеклист нужно отправить пустой ПОСТ запрос на http://127.0.0.1:8000/api/v1/logout/:

* Таким образом access токен истечет и возможности его обновить без процедуры login не будет.


4) Документация по всем эндпоинтам:

* копируем все содержимое файла schema.yaml
* идем на https://editor.swagger.io/ и вставляем в редактор
* получаем полный swagger api documentation
