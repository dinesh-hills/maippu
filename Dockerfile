FROM python:3.10.9-alpine3.17
WORKDIR /app
COPY . .
EXPOSE 8000
RUN pip install pipenv
RUN pipenv install