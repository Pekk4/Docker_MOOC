FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

EXPOSE 80

RUN apt update && apt install -y apache2 php libapache2-mod-php php-mysql php-g$
RUN chown www-data:www-data /var/www/html

CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]
