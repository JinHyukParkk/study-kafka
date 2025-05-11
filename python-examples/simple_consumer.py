from kafka import KafkaConsumer
import json

def json_deserializer(data):
    return json.loads(data.decode('utf-8'))

# Kafka 컨슈머 인스턴스 생성
consumer = KafkaConsumer(
    'example-topic-python',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    group_id='my-python-consumer-group',
    value_deserializer=json_deserializer
)

print("Consumer started. Waiting for messages...")

try:
    # 메시지 소비
    for message in consumer:
        print(f"Received Message - Topic: {message.topic}, Partition: {message.partition}, Offset: {message.offset}")
        print(f"Key: {message.key}, Value: {message.value}")
        print("-------------------------------------")
        
except KeyboardInterrupt:
    print("Consumer stopped by user")
    
finally:
    # 리소스 정리
    consumer.close()
    print("Consumer closed")
