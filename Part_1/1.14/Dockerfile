FROM ruby:2.6.0

WORKDIR /app
COPY . .

EXPOSE 3000

RUN apt update && apt install -y nodejs
RUN bundle install

RUN rails db:migrate
CMD rails s

