# study-kafka

Kafka 학습 코드 및 예제

## 프로젝트 구조

- **java-examples**: Java를 사용한 Kafka 프로듀서 및 컨슈머 예제
- **python-examples**: Python을 사용한 Kafka 프로듀서 및 컨슈머 예제

## 개요

Apache Kafka는 고성능, 확장성, 내구성이 뛰어난 분산 이벤트 스트리밍 플랫폼입니다. 이 레포지토리는 Kafka의 기본 개념과 사용 방법을 학습하기 위한 예제 코드를 포함하고 있습니다.

## 주요 개념

1. **프로듀서(Producer)**: 메시지를 생성하여 토픽에 게시하는 애플리케이션
2. **컨슈머(Consumer)**: 토픽으로부터 메시지를 구독하고 처리하는 애플리케이션
3. **토픽(Topic)**: 메시지가 저장되는 카테고리 또는 피드 이름
4. **파티션(Partition)**: 토픽이 분할되는 단위, 병렬 처리를 가능하게 함
5. **브로커(Broker)**: Kafka 서버, 여러 브로커가 클러스터를 구성

## 예제 실행을 위한 로컬 Kafka 설정

### Docker를 사용한 설정

```bash
# docker-compose.yml 파일 생성
docker-compose up -d
```

### Docker Compose 파일 예시

```yaml
version: '3'
services:
  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000
    ports:
      - "2181:2181"

  kafka:
    image: confluentinc/cp-kafka:latest
    depends_on:
      - zookeeper
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
```

## 참고 자료

- [Apache Kafka 공식 문서](https://kafka.apache.org/documentation/)
- [Confluent Kafka 문서](https://docs.confluent.io/platform/current/overview.html)
