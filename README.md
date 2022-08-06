# Проект "YaMDb"

версия c Docker, Continuous Integration на GitHub Actions

развернут по адресу http://84.252.138.138

![yamdb_workflow](https://github.com/sarvilin/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Описание
Проект YaMDb собирает отзывы пользователей на произведения.

Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Список категорий может быть расширен.
Произведению может быть присвоен жанр из списка предустановленных.
Новые жанры может создавать только администратор.

Сами произведения в YaMDb не хранятся.

Читатели оставляют к произведениям текстовые отзывы и выставляют
произведению рейтинг (оценку в диапазоне от одного до десяти). 
По оценкам автоматически высчитывается средняя оценка произведения.

Полная документация к API:  http://84.252.138.138/redoc


###  Технологии
- Python 3.7
- Django 2.2.19
- DjangoREST framework 3.12.4
- JWT


## Установка на локальном компьютере
Эти инструкции помогут вам создать копию проекта и запустить ее на локальном компьютере для целей разработки и тестирования.

### Установка Docker
Установите Docker, используя инструкции с официального сайта:
- для [Windows и MacOS](https://www.docker.com/products/docker-desktop)
- для [Linux](https://docs.docker.com/engine/install/ubuntu/). Отдельно потребуется установть [Docker Compose](https://docs.docker.com/compose/install/)

### Запуск проекта (на примере Linux)

- Склонируйте в текущую папку `git clone https://github.com/sarvilin/yamdb_final`
- Перейдите в папку `cd yamdb_final`
- Создайте файл `.env` командой `touch .env` и добавьте в него переменные окружения для работы с базой данных:
```
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД 
```
- Запустите docker-compose командой `sudo docker-compose up -d`


## Деплой на удаленный сервер
Для запуска проекта на удаленном сервере необходимо:
- скопировать на сервер файлы `docker-compose.yaml`, `.env` и папку `nginx` командами:
(поскольку на сервер деплоятся только контейнеры - db, web, nginx, это в задании так)
```
scp docker-compose.yaml  <user>@<server-ip>:
scp .env <user>@<server-ip>:
scp -r nginx/ <user>@<server-ip>:

```
- создать переменные окружения в разделе `secrets` настроек текущего репозитория:
```
DOCKER_PASSWORD # Пароль от Docker Hub
DOCKER_USERNAME # Логин от Docker Hub
HOST # Публичный ip адрес сервера
USER # Пользователь зарегистрированный на сервере
PASSPHRASE # Если ssh-ключ защищен фразой-паролем
SSH_KEY # Приватный ssh-ключ
TELEGRAM_TO # ID телеграм-аккаунта
TELEGRAM_TOKEN # Токен бота
```

### После каждого обновления репозитория (`git push`) будет происходить:
1. Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8) и запуск pytest из репозитория yamdb_final
2. Сборка и доставка докер-образов на Docker Hub.
3. Автоматический деплой.
4. Отправка уведомления в Telegram.


## После запуска проекта необходимо:

- Сделать миграции `sudo docker-compose exec web python manage.py migrate`
- Соберите статику командой `sudo docker-compose exec web python manage.py collectstatic --no-input`
- Создайте суперпользователя Django `sudo docker-compose exec web python manage.py createsuperuser`
- Загрузите данные в базу данных при необходимости `sudo docker-compose exec web python3 manage.py ProcessCsv`

## Участники:

[Сарвилин Алексей.](https://github.com/sarvilin/yamdb_final) 
- Категории (Categories), жанры (Genres) и произведения (Titles): модели, view и эндпойнты для них и рейтинги. 
- Докеризация, разработка процесса CI (непрерывной интеграции) с использованием GitHub Actions. 
- Подготовка  к production и deploy на YandexCloud.

[Панасенков Денис.](https://github.com/uchastnik/api_yamdb)
Управление пользователями (Auth и Users): система регистрации и аутентификации, права доступа, работа с токеном, система подтверждения e-mail, поля.

[Анучин Антон.](https://github.com/Homer-Ford/yamdb_final)
Отзывы (Review) и комментарии (Comments): модели и view, эндпойнты, права доступа для запросов. Рейтинги произведений.