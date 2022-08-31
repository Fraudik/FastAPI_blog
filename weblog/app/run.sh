#!/bin/sh

# create actual revision if it's missing
# alembic revision --autogenerate -m 'Create DB'

# apply revisions
alembic upgrade head


export APP_MODULE=${APP_MODULE-data.main:app}
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8001}

exec gunicorn --bind $HOST:$PORT "$APP_MODULE" -k uvicorn.workers.UvicornWorker