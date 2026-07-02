# HANDSON 10: Microservices Decomposition Architecture

## Bounded Context Strategy Mapping
* **API Gateway (Port 5000):** Proxy routing layer. Acts as the single point of entry.
* **Course Service (Port 5001):** Manages course records independently via `courses.db`.
* **Student Service (Port 5002):** Manages student records and handles enrollment checks via `students.db`.

## Synchronous HTTP vs. Asynchronous Message Queue Trade-offs
* **Synchronous HTTP (Used here):** Simple to implement but causes tight operational coupling. If the Course Service goes down, the Student Service enrollment system crashes with a 503 error immediately.
* **Asynchronous Message Queues (RabbitMQ/Kafka):** Decouples services so they don't depend on each other being online at the same millisecond. Offers high resilience, but introduces eventual consistency and infrastructure complexity.