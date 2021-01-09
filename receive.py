import pika, os, time


def data_process_function(msg):
    print(" Received Data")
    print(" [x] Received " + str(msg))

    time.sleep(5)  # delays for 5 seconds
    print(" DATA processing finished")
    return


# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = "amqps://wotmrxyh:HGXgcb5u1qVWF6jQHgscxXKqSFa3PRS2@hawk.rmq.cloudamqp.com/wotmrxyh"
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()  # start a channel


# create a function which is called on incoming messages
def callback(ch, method, properties, body):
    data_process_function(body)
    ch.basic_ack(delivery_tag = method.delivery_tag)



channel.queue_declare(queue='Yosbel', durable=True)
channel.basic_qos(prefetch_count=1)

# set up subscription on the queue
channel.basic_consume('Yosbel',
                      callback)

# start consuming (blocks)
channel.start_consuming()
connection.close()
