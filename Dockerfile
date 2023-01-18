FROM python:3.10.9-alpine3.17
WORKDIR /app
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv
RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_EMAIL=admin@maippu.in
ENV DJANGO_SUPERUSER_PASSWORD=admin
COPY . .
RUN ./manage.py makemigrations
RUN ./manage.py migrate
EXPOSE 8000
CMD [ "sh", "runserver.sh" ]