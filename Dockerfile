FROM ubuntu:latest

WORKDIR /app
COPY . /app

CMD [ "./test.sh" ]