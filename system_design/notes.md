# 🏗️ System Design Interview Notes

## 1. What Is System Design?
System design is the process of defining the architecture, components, modules, interfaces, and data flow of a system to satisfy specified requirements. In interviews, it's about designing scalable, reliable, and maintainable systems.

---

## 2. Key Concepts

### ⚙️ Scalability
- **Vertical scaling**: Adding more power (CPU, RAM) to a single machine.
- **Horizontal scaling**: Adding more machines to handle load.

### 🧱 Load Balancing
- Distributes traffic across multiple servers.
- Common algorithms: Round Robin, Least Connections, IP Hash.

### 🗃️ Caching
- Reduces latency and load on backend.
- Tools: Redis, Memcached.
- Cache strategies: Write-through, Write-around, Write-back.

### 🛢️ Database Design
- **SQL**: Structured, relational, ACID-compliant.
- **NoSQL**: Flexible schema, scalable, eventual consistency.
- **Sharding**: Splitting data across multiple databases.

### 📨 Message Queues
- Decouple services and handle asynchronous tasks.
- Tools: Kafka, RabbitMQ, AWS SQS.

### 🧭 Consistency Models
- **Strong consistency**: All nodes see the same data at the same time.
- **Eventual consistency**: Nodes converge to the same data over time.

---

## 3. Common Interview Questions

- Design a URL shortening service (like Bitly)
- Design a scalable chat system (like WhatsApp)
- Design an e-commerce platform
- Design a ride-sharing service (like Uber)
- Design a news feed system (like Facebook)

---

## 4. Tips for Interviews

- Clarify requirements before jumping into design.
- Discuss trade-offs (latency vs consistency, SQL vs NoSQL).
- Use diagrams to explain architecture.
- Think about bottlenecks and failure points.
- Mention monitoring, logging, and security.

---

## 5. Resources

- [System Design Primer](https://github.com/donnemartin/system-design-primer)
- [Grokking the System Design Interview](https://www.educative.io/courses/grokking-the-system-design-interview)
- [Awesome Scalability](https://github.com/binhnguyennus/awesome-scalability)
