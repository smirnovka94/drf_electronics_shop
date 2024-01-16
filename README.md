# Онлайн платформа торговой сети электроники
Веб-приложение с API интерфейсом и админ-панелью.

## Описание проекта
Сеть представляет собой иерархическую структуру из 3 уровней [Завод, Розничная сеть, Индивидуальный предприниматель]
Каждое звено сети ссылается только на одного поставщика оборудования
Есть возможность указать несколько товаров для одного Завода или Розничной цепи.
При создании Узла торговой сети время создания (заполняется автоматически)
при отображении 

Настроены права доступа к API так, чтобы только активные сотрудники имели доступ к API.

### Набор представлений
В представлении Элементов торговой цепи отображается вложенный список товаров этой цепи
Добавлена возможность фильтрации объектов по определенной стране

### Валидация
Завод - не имеет возможности ссылаться на поставщика
Завод - не имеет возможности указывать задолженность перед поставщиком
Для модели поставщика исключена возможность редактирования параметра <Задолженость перед поставщиком>

### Админ-панель
Настроено отображение [Звена торговой цепи, Продуктов, Пользователей, Группы пользователей]

#### В модели Звеньев торговой цепи:
Добавлена ссылка на «Поставщика»
Добавлен фильтр по названию города
Добавлен «admin action», очищающий задолженность перед поставщиком у выбранных объектов

# Установка и использование
#### Клонируем репозиторий

#### Устанавливаем виртуальное окружение 
```
python -m venv venv
```
#### Запускаем виртуальное окружение
```
venv\Scripts\activate.bat
```
#### Устанавливаем библиотеки
```
pip install -r requirements.txt
```

Создаем базу данных в PgAdmin с именем <drf_electronics_shop>
#### Создаем файл <.env>
.env.template переименовать на .env

#### Выполнить миграции
```
python manage.py makemigrations
python manage.py migrate
```
#### Загрузить базу данных
добавить неактивного пользователя
```
python manage.py users_data
```
добавить значения остальных моделей
```
python manage.py link_data   
python manage.py product_data
```

Создаем superuser
login: kirill@sky.pro
password: qwerty88
```
python manage.py super_user
```