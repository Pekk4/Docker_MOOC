# For production version:

FROM ruby:2.6.0

WORKDIR /app
COPY . .

EXPOSE 3000

RUN apt update && apt install -y nodejs
RUN bundle install

RUN rails credentials:edit
RUN EDITOR="mate --wait" bin/rails credentials:edit
RUN rails db:migrate RAILS_ENV=production
RUN rake assets:precompile

CMD rails s -e production

# This requires to delete file config/credentials.yml.enc from repo and 
# change line 23 value to 'true' from 'ENV['RAILS_SERVE_STATIC_FILES'].present?' at config/environments/production.rb before building the docker image.
#
# I have never used Ruby nor RoR before this exercise and I'm not sure at all about that being a good solution for this. But at least it works, so far, so good. 


# And the one for development version. This works without any changes on repos files. 
# 
# FROM ruby:2.6.0
#
# WORKDIR /app
# COPY . .
#
# EXPOSE 3000
#
# RUN apt update && apt install -y nodejs
# RUN bundle install
#
# RUN rails db:migrate
# CMD rails s
