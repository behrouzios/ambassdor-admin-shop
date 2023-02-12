FROM python:3.9-slim
ENV  PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR  /app
COPY . /app
RUN apt-get update && \
      apt-get -y install sudo 
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential  -y 
RUN pip3 install -r requirements.txt
CMD python3 manage.py wait_for_db && python3 manage.py runserver 0.0.0.0:8000