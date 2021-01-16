<<<<<<< Updated upstream
Docker hub link: https://hub.docker.com/r/p3xu/apache2-php

Haven't programmed very much yet, so neither have I particular 'favorite programming environment' either (yet). However, didn't want to skip this exercise and because I have made some small scale PHP applications in the early 2010s, I decided to create the environment I used the sqlite instead of mysql this time (although there is also php's mysql-extension installed), because it would be a way smarter to use mysql from it's own container and I'm not familiar yet with using compose.
=======
Haven't programmed very much yet, so neither have I particular 'favorite programming environment' either (yet). However, didn't want to skip this exercise and because I have made some small scale PHP applications in the early 2010s, I decided to create the environment that I used back then.
I used the sqlite instead of mysql this time (although there is also php's mysql-extension installed), because it would be a way smarter to use mysql from it's own container and I'm not familiar yet with using compose.
>>>>>>> Stashed changes

Image's readme:

This image contains apache2 and php installed on ubuntu:latest with mysql, sqlite, gd and imagick extensions.

To run the container:

docker run -d -v $(pwd):/var/www/html p3xu/apache2-php

Run the command from your working directory, so it will bind mount your php files to the www-dir. Using -d flag runs the container detached.

