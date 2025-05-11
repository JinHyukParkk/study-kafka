# Kafka Java 예제

이 디렉토리는 Java를 사용한 Kafka 프로듀서 및 컨슈머 예제를 포함하고 있습니다.

## 필요 조건

- Java 11 이상
- Maven
- Kafka 서버 (로컬 또는 원격)

## 실행 방법

### Maven으로 의존성 설치

```bash
mvn clean install
```

### 프로듀서 실행

```bash
java -cp target/kafka-examples-1.0-SNAPSHOT.jar:target/dependency/* SimpleKafkaProducer
```

### 컨슈머 실행

```bash
java -cp target/kafka-examples-1.0-SNAPSHOT.jar:target/dependency/* SimpleKafkaConsumer
```

## 코드 설명

### SimpleKafkaProducer.java

- Kafka 프로듀서 설정 및 인스턴스 생성
- 'example-topic'에 10개의 메시지 전송
- 각 메시지는 key와 value를 가짐
- 비동기적으로 메시지 전송 후 콜백을 통해 결과 확인

### SimpleKafkaConsumer.java

- Kafka 컨슈머 설정 및 인스턴스 생성
- 'example-topic'을 구독
- 지속적으로 메시지를 폴링하여 수신된 메시지 처리
- 각 메시지의 토픽, 파티션, 오프셋, 키, 값 등의 정보 출력
