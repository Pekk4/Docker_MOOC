FROM golang:1.16-buster

WORKDIR /app

COPY . /app

EXPOSE 8080

ENV REQUEST_ORIGIN=http://localhost:5000

RUN go build

CMD ./server
