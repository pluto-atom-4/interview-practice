# 🔗 System Design: URL Shortener

## 🧭 Overview
Design a scalable service that converts long URLs into short, shareable links — similar to Bitly or TinyURL.

---

## 🎯 Requirements

### Functional
- Shorten a long URL
- Redirect short URL to original
- Track usage (clicks, timestamps)
- Optional: custom aliases, expiration, user accounts

### Non-Functional
- High availability
- Low latency redirection
- Horizontal scalability
- Rate limiting and abuse prevention

---

## 🧱 Architecture Components

| Layer       | Component                     | Description |
|------------|-------------------------------|-------------|
| Frontend    | React / Vue / Angular         | Form to submit and retrieve URLs |
| Backend     | REST API (Node.js / Django / Spring) | Handles URL creation and redirection |
| Database    | PostgreSQL / MongoDB          | Stores mappings and metadata |
| Cache       | Redis                         | Speeds up redirection lookups |
| ID Generator| Base62 encoder or hash        | Generates short unique keys |
| Hosting     | AWS / GCP / Azure             | Scalable deployment |
| Monitoring  | Prometheus + Grafana          | Tracks performance and errors |

---

## 🔄 API Design

### POST `/api/shorten`
```json
{
  "longUrl": "https://example.com/very/long/url"
}
```
### GET `/abc123`

Behavior: Redirects to original long URL


## 🗃️ Database Schema (SQL)

```sql
CREATE TABLE urls (
  id SERIAL PRIMARY KEY,
  short_code VARCHAR(10) UNIQUE NOT NULL,
  long_url TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  click_count INT DEFAULT 0
);
```

This snippet defines a simple schema for storing shortened URLs, including a unique short code, the original long URL, a timestamp, and a click counter. Let me know if you’d like to expand it with expiration dates, user IDs, or indexing strategies!

## 🔢 Short Code Generation

### Option 1: Base62 Encoding
- Encode auto-incremented ID using [A-Za-z0-9]
- Example: ID `125` → `abc`

### Option 2: Hashing
- Hash long URL and truncate
- Handle collisions with retries or salt

## 🚀 Performance & Scalability

- **Caching**: Use Redis for short-to-long URL lookup
- **Rate Limiting**: Token bucket or IP throttling
- **Load Balancing**: NGINX or cloud-native balancer
- **Replication**: Read replicas for DB scaling
- **CDN**: Serve static assets and redirect logic globally

## 📊 Analytics & Monitoring

- Track:
  - Clicks per URL
  - Referrer and geolocation
  - Time of access
- Tools:
  - Prometheus for metrics
  - Grafana for dashboards
  - ELK stack for logs

## 🧪 Testing Strategy

- Unit tests for API endpoints
- Integration tests for DB and cache
- Load testing with JMeter or Locust
- Security tests for abuse and injection


## 🧠 Interview Tips

- Start with requirements and constraints
- Use diagrams to show data flow
- Discuss trade-offs (SQL vs NoSQL, hash collisions, cache eviction)
- Mention deployment, logging, and monitoring

## 🎤 Mock Interview Questions

### 🟢 Beginner

#### System Design
- How would you design a URL shortening service like Bitly?
- What are the key components of a full stack web application?
- What is the difference between frontend and backend responsibilities?
- How would you store and retrieve URL mappings in a database?
- What is caching and why is it useful?

#### Full Stack Integration
- How would you build the frontend for submitting and retrieving shortened URLs?
- What security measures would you implement in the frontend and backend?
- How would you handle form validation and error feedback in the UI?

---

### 🟡 Intermediate

#### System Design
- What are the trade-offs between using SQL and NoSQL for storing URL mappings?
- How would you handle hash collisions in short code generation?
- How would you scale the redirection service to handle millions of requests per day?
- What caching strategy would you use to optimize performance?
- How would you implement rate limiting to prevent abuse?

#### Full Stack Integration
- How would you integrate authentication for user-specific URL tracking?
- How would you test the full stack end-to-end?
- How would you design the system to support custom short codes?

---

### 🔴 Advanced

#### System Design
- What changes would you make to support analytics and reporting?
- How would you ensure high availability and fault tolerance?
- How would you deploy and monitor this system in production?
- How would you extend the system to support QR code generation?
- How would you handle expired or deleted URLs?
- How would you migrate this system from monolith to microservices?

#### Full Stack Integration
- How would you implement real-time analytics in the frontend?
- How would you design a dashboard for tracking URL performance?
- How would you optimize frontend performance for high traffic?



### Bonus
- How would you extend the system to support QR code generation?
- How would you handle expired or deleted URLs?
- How would you migrate this system from monolith to microservices?

