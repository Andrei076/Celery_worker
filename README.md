
docker run -d -p 5672:5672 -p 15672:15672 rabbitmq:3-management

celery -A celery_worker worker --loglevel=INFO --purge --pool=solo