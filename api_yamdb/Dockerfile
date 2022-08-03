FROM python:3.7-slim

WORKDIR /app
COPY . .
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r api_yamdb/requirements.txt --no-cache-dir
CMD ["gunicorn", "api_yamdb/api_yamdb.wsgi:application", "--bind", "0:8000" ]


#COPY ./ /app
#RUN python3 -m pip install --upgrade pip
#RUN pip install -r /app/api_yamdb/requirements.txt --no-cache-dir
#WORKDIR /app/api_yamdb/
#CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]


#WORKDIR /app/api_yamdb
#COPY requirements.txt ./
#RUN pip3 install -r requirements.txt --no-cache-dir
#COPY . .
#CMD ["gunicorn", "api_yamdb.api_yamdb.wsgi:application", "--bind", "0:8000" ]


## Запустить команду создания директории внутри контейнера
#RUN mkdir /app
#
## Скопировать с локального компьютера файл зависимостей в директорию /app.
#COPY api_yamdb/requirements.txt /app
#
## Выполнить установку зависимостей внутри контейнера.
#RUN pip3 install -r requirements.txt --no-cache-dir
#
## Скопировать содержимое директории /api_yamdb c локального компьютера в директорию /app.
#COPY api_yamdb/ /app
#
## Сделать директорию /app рабочей директорией.
#WORKDIR /app
#
## Выполнить запуск сервера разработки при старте контейнера.
##CMD ["python3", "manage.py", "runserver", "0:8000"]
#CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]