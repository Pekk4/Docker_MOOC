FROM python:3.9-alpine AS base

FROM base AS build-stage

WORKDIR /app

COPY . .

RUN pip install --prefix=/dependencies -r requirements.txt
RUN adduser -D -u 16661 app

RUN rm -rf requirements.txt README.md .github Dockerfile*

FROM base

WORKDIR /home/app

COPY --from=build-stage /dependencies /usr/local
COPY --from=build-stage /etc/passwd /etc/passwd
COPY --from=build-stage /app .

EXPOSE 5000

USER app

CMD [ "gunicorn", "app:app",  "--bind", "0.0.0.0:5000" ]