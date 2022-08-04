# Проект "YaMDb"

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

Полная документация к API находится в /redoc

При запущенном проекте:
http://localhost/redoc/

###  Технологии
- Python 3.7
- Django 2.2.19
- DjangoREST framework 3.12.4
- JWT

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/sarvilin/infra_sp2.git
```
```
cd infra_sp2
```

Создать env-файл (infra_sp2/infra/.env) по шаблону: 
```
DEBUG=1
SECRET_KEY='<ВАШ СЕКРЕТНЫЙ КЛЮЧ DJANGO'
ALLOWED_HOSTS=localhost ['*']
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

Запуcтить проект в docker:
```
cd infra
```
```
sudo docker-compose up -d --build 
```

Создать миграции, создать superuser, собрать статику:
```
sudo docker-compose exec web python3 manage.py migrate
```
```
sudo docker-compose exec web python3 manage.py createsuperuser
```
```
sudo docker-compose exec web python3 manage.py collectstatic --no-input 
```

Запустить скрипт первоначального заполнения базы (если нужно):
```
sudo docker-compose exec web python3 manage.py ProcessCsv
```

После запуска проект доступен по URL:
```
http://localhost/
```

### Авторы
```
Панасенков Денис
Сарвилин Алексей
Анучин Антон
```
