FROM python:3.10.4-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y git

COPY builder.py requirements.txt ./

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python", "builder.py" ]
