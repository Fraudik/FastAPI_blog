# FastAPI_blog
Asynchronous blog backend with FastAPI and PostgreSQL

## Setup and launch

### Manually
  1. Move to /app directory (cd app)
  2. Use command ```poetry install```
  (you can install poetry with pip or another way: https://python-poetry.org/docs/#installation)
  3.1. For Windows users use command ```poetry run python data/main.py``` 
  3.2. For Unix users use command ```poetry run ./run.sh```
To stop running the app, press CTRL+C

### With Docker
  1. First install Docker: https://www.docker.com/
  2. Use command ```docker-compose -f docker-compose.local.yml up -d```
  (it can take some time)

##

After this you can visit http://localhost:8001/ or http://127.0.0.1:8001/

Also documentation is available at /docs (http://.../docs)
