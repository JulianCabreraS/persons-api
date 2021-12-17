from kafka import KafkaConsumer

TOPIC_NAME = 'persona'
KAFKA_SERVER = 'kafka:9092'

consumer = KafkaConsumer(TOPIC_NAME,
                         bootstrap_servers=KAFKA_SERVER,
                         enable_auto_commit=True,
                         group_id='my-group')
for message in consumer:
    print(message)
