FROM python:3.8-slim-buster
# light-weight Linux OS

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD = ["python" , "demo/manage.py" , "runserver" , "0.0.0.0:8000"]

