import pika
from logging import basicConfig
# from data import data
import json
from getRates import getRates

basicConfig()

url = "amqps://wotmrxyh:HGXgcb5u1qVWF6jQHgscxXKqSFa3PRS2@hawk.rmq.cloudamqp.com/wotmrxyh"
params = pika.URLParameters(url)
# params.socket_timeout = 5


data = getRates()
print(data)


connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
# channel.queue_declare(queue='Yosbel', durable: true,) # Declare a queue
# send a message

channel.basic_publish(
            exchange = '',
            routing_key = 'Yosbel',
            body = json.dumps(data)
            properties = pika.BasicProperties(
                delivery_mode = 2
            ))
print("[x] Message sent to consumer")
connection.close()
