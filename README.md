# Онлайн платформа торговой сети электроники
# Установка и использование
Клонируем репозиторий

Устанавливаем виртуальное окружение 
```
python -m venv venv
```
Запускаем Виртуальнео окружение
```
venv\Scripts\activate.bat
```
Устанавливаем библиотеки
```
pip install -r requirements.txt
```

Создаем базу данных в PgAdmin с именем <drf_electronics_shop>
### Создаем файл<.env>
.env.template переименовать на .env

#### Выполнить миграции
```
python manage.py makemigrations
python manage.py migrate
```
Загрузить базу данных
добавить неактивного пользователя
```
python manage.py users_data

```
Создаем superuser
login: kirill@sky.pro
password: qwerty88
```
python manage.py super_user
```