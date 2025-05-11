# Kafka Python 예제

이 디렉토리는 Python을 사용한 Kafka 프로듀서 및 컨슈머 예제를 포함하고 있습니다.

## 필요 조건

- Python 3.6 이상
- kafka-python 라이브러리
- Kafka 서버 (로컬 또는 원격)

## 설치

필요한 패키지를 설치합니다:

```bash
pip install -r requirements.txt
```

## 실행 방법

### 프로듀서 실행

```bash
python simple_producer.py
```

### 컨슈머 실행

```bash
python simple_consumer.py
```

## 코드 설명

### simple_producer.py

- Kafka 프로듀서 설정 및 인스턴스 생성
- JSON 형식으로 메시지 직렬화
- 'example-topic-python'에 10개의 JSON 메시지 전송
- 각 메시지는 ID, 메시지 내용, 타임스탬프 포함

### simple_consumer.py

- Kafka 컨슈머 설정 및 인스턴스 생성
- JSON 형식으로 메시지 역직렬화
- 'example-topic-python' 토픽 구독
- 수신된 메시지의 토픽, 파티션, 오프셋, 키, 값 등의 정보 출력
