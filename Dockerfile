FROM python:2.7-slim

WORKDIR /app
COPY . /app

CMD [ "./test.sh" ]