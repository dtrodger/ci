FROM python:2.7-slim

WORKDIR /app
COPY . /app

CMD [ "bash", "test.sh" ]