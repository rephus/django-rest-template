

# This is our custom base django image. It is built from:
# https://github.com/networklocum/django-microservice-template/blob/master/Dockerbuild
FROM python:3.7-alpine

EXPOSE 8000

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
#RUN apt-get update && apt-get install -y libpq-dev gcc python3-dev musl-dev

ADD ./project /code
WORKDIR /code

RUN pip install \
    djangorestframework==3.9.0 \
    django-rest-swagger==2.2.0 \
    django-extensions==2.1.4 \
    markdown==3.0.1 \
    psycopg2-binary==2.7.6.1 \
    django-filter==2.0.0 \ 
    faker==1.0.1 \ 
    factory-boy==2.11.1

CMD  python init.py && python manage.py runserver 0.0.0.0:8000
#CMD python entrypoint.py