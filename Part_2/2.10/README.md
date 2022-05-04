Only thing that I had to change was to set backend's REQUEST_ORIGIN env value to just localhost without frontend's port, because of nginx the request now comes from it instead of frontend or something, I think.

The Dockerfiles has those env values from part 1 exercise, but `docker-compose.yml`'s values overrides them, if set.

The Dockerfiles I used are exactly the same as they were in the exercise 2.3.

[Frontend's Dockerfile](../2.3/frontend/Dockerfile):

```Dockerfile
FROM node:16-bullseye-slim

WORKDIR /app

COPY . /app

EXPOSE 5000

ENV REACT_APP_BACKEND_URL=http://localhost:8080

RUN npm install
RUN npm run build
RUN npm install -g serve

CMD [ "serve", "-s", "-l", "5000", "build" ]
```

[Backend's Dockerfile](../2.3/backend/Dockerfile):

```Dockerfile
FROM golang:1.16-buster

WORKDIR /app

COPY . /app

EXPOSE 8080

ENV REQUEST_ORIGIN=http://localhost:5000

RUN go build

CMD ./server
```

