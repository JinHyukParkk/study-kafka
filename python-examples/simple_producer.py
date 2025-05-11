from kafka import KafkaProducer
import json
import time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

# Kafka 프로듀서 인스턴스 생성
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=json_serializer
)

# 토픽 이름
topic_name = 'example-topic-python'

# 메시지 전송
for i in range(10):
    data = {
        'id': i,
        'message': f'This is message {i}',
        'timestamp': time.time()
    }
    
    future = producer.send(topic_name, value=data)
    
    try:
        # 메시지 전송 결과 확인
        record_metadata = future.get(timeout=10)
        print(f"Message sent to {record_metadata.topic} partition {record_metadata.partition} offset {record_metadata.offset}")
    except Exception as e:
        print(f"Error sending message: {e}")
    
    # 잠시 대기
    time.sleep(0.5)

# 리소스 정리
producer.flush()
producer.close()

print("Producer completed")
