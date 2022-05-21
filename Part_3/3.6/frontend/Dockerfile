FROM node:16-alpine3.15 AS build-stage

WORKDIR /app

ENV REACT_APP_BACKEND_URL=http://localhost:8080

COPY . .

RUN npm install && npm run build

RUN adduser -D frontend

FROM nginx:alpine

COPY --from=build-stage /app/build/ /usr/share/nginx/html

EXPOSE 80
