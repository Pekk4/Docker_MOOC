FROM ubuntu:latest

WORKDIR /app
COPY . /app

EXPOSE 8000/tcp

RUN apt update && apt install -y curl 
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash
RUN apt install -y nodejs
RUN npm install

CMD npm start
