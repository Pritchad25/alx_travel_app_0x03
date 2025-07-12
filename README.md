## Background Email Notifications

This project uses Celery with RabbitMQ to send booking confirmation emails asynchronously.

### Setup

- Start RabbitMQ:
  `docker run -d --hostname rabbitmq --name rabbitmq -p 5672:5672 rabbitmq:3-management`

- Run Celery worker:
  `celery -A alx_travel_app worker --loglevel=info`
