# YES123 爬蟲

## Dependencies

1. Python 3.5+
1. pip
1. Docker

## Getting Started

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

# Start Rabbitmq
docker run --name some-rabbitmq -p 15672:15672 -p 5672:5672 -e RABBITMQ_USERNAME=celery -e RABBITMQ_PASSWORD=celery -d bitnami/rabbitmq:latest

# Start RethinkDB
docker run --name some-rethink -p 28015:28015 -p 8080:8080 -v "$PWD:/data" -d rethinkdb:2.3.6

# Start celery worker, c is the concurrency level
celery -A tasks worker -c 4 --loglevel=info

# In another terminal
source venv/bin/activate

# Launch job manually
python yes123.py

```

Add the job dispatcher in crontab for automatic job dispatch
```
# crontab
* * * * * python yes123.py
```