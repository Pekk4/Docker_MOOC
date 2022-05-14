# Instructions

First, clone the repository. Then set your Docker Hub username and token to `.env` file:

```
DHUB_USER=<username>
DHUB_TOKEN=<token>
```

Next, build the container:

```bash
docker-compose build
```

Usage:

```bash
docker-compose run builder [repository]
```

Example, which builds [Heroku CI/CD example project](https://github.com/Pekk4/turbo-octo-bassoon) and pushes it to Docker Hub:

```bash
docker-compose run builder https://github.com/Pekk4/turbo-octo-bassoon.git
```

## Tested with

The project is tested and working at least with the following repositories:

 - https://github.com/Pekk4/turbo-octo-bassoon
 - https://github.com/Pekk4/docker-hy-frontend-example
 - https://github.com/Pekk4/docker-hy-backend-example
 - https://github.com/Pekk4/ajoneuvodata

These repositories will be deleted later.
