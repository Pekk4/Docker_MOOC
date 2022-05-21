FROM golang:1.16.15-alpine3.15 AS build-stage

WORKDIR /app

COPY . .

RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -ldflags="-w -s" -o /app/server

RUN adduser -D backend

FROM scratch

WORKDIR /home/backend

ENV REQUEST_ORIGIN=http://localhost:5000

EXPOSE 8080

COPY --from=build-stage /app/server /home/backend/server
COPY --from=build-stage /etc/passwd /etc/passwd

USER backend

CMD ["./server"]
