FROM ubuntu

RUN apt-get update && apt-get install -qq -y python-pip python-dev uwsgi nano

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN bash ./test.sh

RUN service uwsgi start
