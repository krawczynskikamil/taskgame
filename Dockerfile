FROM python:3.10.4-alpine3.15

WORKDIR /backend

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python3 manage.py test && python manage.py runserver 0.0.0.0:8000