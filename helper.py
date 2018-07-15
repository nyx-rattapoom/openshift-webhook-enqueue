import pika
import os
import json


def get_headers_dict(headers):
    headers_dict = dict()
    for key, value in headers.items():
        headers_dict[key] = value
    return headers_dict


def get_amqp_params():
    url = os.environ.get('CLOUDAMQP_URL', 'amqp://dev@localhost/line-api-enqueue')
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    return params


def send_queue(fpika, message):
    if isinstance(message, dict):
        message = json.dumps(message)

    channel = fpika.channel()
    channel.queue_declare(queue='line')
    channel.basic_publish(exchange='', routing_key='line', body=message)
    fpika.return_channel(channel)