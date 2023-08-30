FROM python:3.8
WORKDIR /Django/app
COPY ./myapp/requirements.txt /Django/app/requirements.txt
COPY ./myapp/manage.py /Django/app/manage.py
RUN pip install -r requirements.txt
EXPOSE 80