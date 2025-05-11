import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.StringSerializer;

import java.util.Properties;

public class SimpleKafkaProducer {
    public static void main(String[] args) {
        // Kafka 브로커 주소 설정
        String bootstrapServers = "localhost:9092";
        
        // Producer 설정
        Properties properties = new Properties();
        properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
        properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        
        // Producer 생성
        KafkaProducer<String, String> producer = new KafkaProducer<>(properties);
        
        // 메시지 전송
        String topic = "example-topic";
        for (int i = 0; i < 10; i++) {
            String key = "key_" + i;
            String value = "message_" + i;
            
            ProducerRecord<String, String> record = new ProducerRecord<>(topic, key, value);
            producer.send(record, (metadata, exception) -> {
                if (exception == null) {
                    System.out.printf("Message sent to topic: %s, partition: %d, offset: %d%n", 
                        metadata.topic(), metadata.partition(), metadata.offset());
                } else {
                    System.err.println("Error sending message: " + exception.getMessage());
                }
            });
        }
        
        // 리소스 정리
        producer.flush();
        producer.close();
        
        System.out.println("Producer completed");
    }
}
