# FastAPI_blog
Weblog backend

#### Author: Blinov Ilya (Fraudik)

Made with:
  - FastAPI
  - PostgreSQL
  - Pydantic
  - SQLAlchemy
  - Docker
  - Alembic
  - Poetry
 

## Setup and launch (requires Docker)

  1. Move to directory with docker-compose.yml
  2. Use command ```docker-compose up -d``` or ```docker-compose up```
  (it can take some time)

How to stop:
  + Use terminal command ```docker-compose stop``` -- if you used command ```docker-compose up -d```
  + Press Ctrl+C -- if you used command ```docker-compose up```

## 

After launching you can visit http://localhost:8001/ or http://127.0.0.1:8001/

Documentation is available at /docs (http://.../docs) or /redoc.

## Swagger screenshot (/docs)
![alt text](https://github.com/Fraudik/FastAPI_blog/blob/stable/docs_example/swagger_screenshot.jpg)
