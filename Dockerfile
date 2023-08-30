FROM python:3.11

WORKDIR /app

# Copy the entire project contents to /app inside the container
COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 8000

# CMD ["python", "demo/manage.py" , "runserver"]
CMD ["python", "/demo/manage.py" , "runserver" , "8000"]