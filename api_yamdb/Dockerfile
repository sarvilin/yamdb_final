FROM python:3.7-slim

WORKDIR /app

COPY . .

RUN python3 -m pip install --upgrade pip

RUN pip3 install -r api_yamdb/requirements.txt --no-cache-dir

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]


#WORKDIR /app/api_yamdb/
#COPY requirements.txt ./
#RUN pip3 install -r requirements.txt --no-cache-dir
#COPY . .
#CMD ["gunicorn", "api_yamdb.api_yamdb.wsgi:application", "--bind", "0:8000" ]