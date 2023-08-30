FROM python:3.8


WORKDIR /DjangoLearn

COPY . /app

RUN pip install -r requirements.txt


EXPOSE 80

CMD ["python" , "/demo/manage.py" , "runserver"]
