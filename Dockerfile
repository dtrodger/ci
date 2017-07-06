FROM ubuntu

RUN apt-get update && apt-get install -y python-pip

WORKDIR /app
COPY . /app

CMD [ "bash", "test.sh" ]