## About

I chose the [project](https://github.com/Pekk4/turbo-octo-bassoon) I made for the exercise 3.1 and which image size with the original Dockerfile is **142MB**.

The project has implemented with Python and at first I tried to find out if it had been possible to use Cython and create just a binary file to run in scratch-container, like I did in the exercise 3.6b. After few hours and still without even getting the simple hello-world POC to work, I gave up and decided to go just with the Python/Alpine. 

I also tried to copy just Python and the dependencies to the scratch-image, like in [this](https://github.com/CrafterKolyan/tiny-python-docker-image/blob/main/Dockerfile.scratch-full), but no success with it. :D

Anyway, I did everything else but used the scratch image and got the image with size **55.2MB**. That scratch-image above with python copied from earlier stage is approx. 32MB, so I think my image is pretty good/not very far from it, when the dependencies and the app itself are still missing from it.

The Dockerfile:

```Dockerfile
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
```