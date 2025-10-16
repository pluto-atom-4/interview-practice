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

| Layer        | Component                            | Description                          |
|--------------|--------------------------------------|--------------------------------------|
| Frontend     | React / Vue / Angular                | Form to submit and retrieve URLs     |
| Backend      | REST API (Node.js / Django / Spring) | Handles URL creation and redirection |
| Database     | PostgreSQL / MongoDB                 | Stores mappings and metadata         |
| Cache        | Redis                                | Speeds up redirection lookups        |
| ID Generator | Base62 encoder or hash               | Generates short unique keys          |
| Hosting      | AWS / GCP / Azure                    | Scalable deployment                  |
| Monitoring   | Prometheus + Grafana                 | Tracks performance and errors        |

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
CREATE TABLE urls
(
    id          SERIAL PRIMARY KEY,
    short_code  VARCHAR(10) UNIQUE NOT NULL,
    long_url    TEXT               NOT NULL,
    created_at  TIMESTAMP DEFAULT NOW(),
    click_count INT       DEFAULT 0
);
```

This snippet defines a simple schema for storing shortened URLs, including a unique short code, the original long URL, a
timestamp, and a click counter. Let me know if you’d like to expand it with expiration dates, user IDs, or indexing
strategies!

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
    - To design a URL shortening service, I would create a backend API that accepts a long URL and returns a short code.
      This short code would be stored in a database along with the original URL. When a user accesses the short URL, the
      service would look up the original URL and redirect the user. I’d use Base62 encoding to generate short codes and
      store mappings in a relational database like PostgreSQL.
- What is the difference between frontend and backend responsibilities?
- How would you store and retrieve URL mappings in a database?
- What is caching and why is it useful?
    - What are the key components of a full stack web application?

#### Full Stack Integration

- How would you build the frontend for submitting and retrieving shortened URLs?
    - I would create a simple form using React or Vue where users can input a long URL. Upon submission, the frontend
      would send a POST request to the backend API and display the returned short URL. I’d also include a section to
      enter a short URL and fetch its original version using a GET request. Styling would be handled with CSS or a UI
      framework like Tailwind or Bootstrap.
- What security measures would you implement in the frontend and backend?
    - On the frontend, I’d validate user input to prevent malformed URLs and use HTTPS to secure communication. I’d also
      sanitize inputs to avoid XSS attacks. On the backend, I’d implement rate limiting, input validation, and
      authentication for protected endpoints.
- How would you handle form validation and error feedback in the UI?
    - I’d use controlled components in React to track input state and validate the URL format using regex. If validation
      fails, I’d show inline error messages. For server-side errors, I’d display toast notifications or alert banners
      with meaningful feedback.

---

### 🟡 Intermediate

#### System Design

- What are the trade-offs between using SQL and NoSQL for storing URL mappings?
    - SQL databases offer strong consistency and structured schema, which is great for enforcing uniqueness and
      relationships. NoSQL databases like MongoDB offer flexibility and horizontal scalability, which can be useful for
      high-volume systems. For a URL shortener, SQL is often preferred for its simplicity and transactional guarantees,
      but NoSQL can be used if scalability is a priority.
- How would you handle hash collisions in short code generation?
- How would you scale the redirection service to handle millions of requests per day?
- What caching strategy would you use to optimize performance?
- How would you implement rate limiting to prevent abuse?
    - I would use a token bucket or leaky bucket algorithm to limit the number of requests per IP address or user within
      a time window. This can be implemented using Redis with expiration keys to track request counts. If the limit is
      exceeded, the API would return a 429 Too Many Requests response.

#### Full Stack Integration

- How would you integrate authentication for user-specific URL tracking?
    - I’d use JWT-based authentication. After login, the frontend would store the token in memory or secure cookies.
      Authenticated requests would include the token in headers. The backend would associate shortened URLs with the
      user ID, and the frontend could fetch a list of URLs created by the logged-in user.
- How would you test the full stack end-to-end?
    - I’d use tools like Cypress or Playwright to simulate user interactions — submitting URLs, receiving short links,
      and verifying redirection. I’d also write integration tests using Jest or Mocha to test API responses and database
      interactions. These tests would run in CI pipelines to ensure reliability.
- How would you design the system to support custom short codes?
    - I’d add an optional input field for custom aliases in the frontend form. The backend would validate uniqueness and
      length constraints before storing it. If the alias is taken, the frontend would show an error and prompt the user
      to choose another.
---

### 🔴 Advanced

#### System Design

- What changes would you make to support analytics and reporting?
- How would you ensure high availability and fault tolerance?
    - I would deploy the service across multiple availability zones using a cloud provider like AWS. Load balancers
      would distribute traffic, and databases would use replication and failover strategies. I’d also use health checks
      and auto-scaling to maintain uptime and recover from failures.
- How would you deploy this system to production?
    - I would containerize the application using Docker to ensure consistency across environments. Each service (
      frontend, backend, database, cache) would run in its own container. I’d use Kubernetes for orchestration, enabling
      auto-scaling, rolling updates, and service discovery.
    - For hosting, I’d choose a cloud provider like AWS, GCP, or Azure. The backend would be deployed behind a load
      balancer (e.g., AWS ALB), and the frontend would be served via a CDN like CloudFront or Cloudflare for fast global
      delivery.
    - CI/CD pipelines would be set up using GitHub Actions or GitLab CI to automate testing, building, and deployment.
      Secrets and environment variables would be managed using a secure vault or the cloud provider’s secret manager.
- How would you ensure zero-downtime deployments?
    - I’d use rolling updates in Kubernetes or blue-green deployments to gradually shift traffic from the old version to
      the new one. Health checks would ensure only healthy pods receive traffic. If an issue is detected, the deployment
      would roll back automatically.
- How would you monitor and log the system in production?
    - I’d use Prometheus to collect metrics and Grafana to visualize them. For logging, I’d use a centralized log
      aggregator like the ELK stack (Elasticsearch, Logstash, Kibana) or a managed service like AWS CloudWatch. Alerts
      would be configured for error rates, latency spikes, and resource usage thresholds.
- How would you handle configuration and secrets?
    - I’d separate configuration from code using environment variables or config maps in Kubernetes. Secrets like API
      keys and database credentials would be stored securely using tools like AWS Secrets Manager, HashiCorp Vault, or
      Kubernetes Secrets, with access restricted by role-based access control (RBAC).

#### Full Stack Integration

- How would you implement real-time analytics in the frontend?
    - I’d use WebSockets or polling to fetch click data in real time. The frontend would display charts using libraries
      like Chart.js or Recharts, updating dynamically as new data arrives. I’d also show breakdowns by location, device,
      and referrer.
- How would you design a dashboard for tracking URL performance?
    - The dashboard would include tables and charts showing metrics like total clicks, daily traffic, top-performing
      URLs, and geographic distribution. I’d use a component-based architecture with reusable widgets and fetch data
      from analytics APIs. Filters and sorting would enhance usability.
- How would you optimize frontend performance for high traffic?
    - I’d use lazy loading for components, code splitting with tools like Webpack, and CDN hosting for static assets.
      I’d also minimize bundle size, compress images, and use caching headers. Monitoring tools like Lighthouse and
      Sentry would help identify bottlenecks.
- How would you migrate this system from monolith to microservices?
    - I’d start by identifying bounded contexts such as URL creation, redirection, analytics, and user management. Each
      would become a separate service with its own database. I’d use an API gateway to route requests and implement
      inter-service communication using REST or messaging queues. Gradual migration with backward compatibility would
      ensure a smooth transition.

### Bonus

#### How would you handle expired or deleted URLs?

To handle expired or deleted URLs, I would introduce metadata fields in the database to track expiration and deletion
status.

##### Database Schema Enhancements:

```sql
ALTER TABLE urls
    ADD COLUMN expires_at TIMESTAMP,
ADD COLUMN is_deleted BOOLEAN DEFAULT FALSE;
```

##### Backend Logic:

- When a short URL is accessed, the backend checks:
    - If `is_deleted = TRUE`, return a 410 Gone response.
    - If `expires_at < NOW()`, return a 404 Not Found or 410 Gone.
- Optionally, log access attempts to expired/deleted URLs for analytics.

##### API Behavior:

- Provide endpoints to:
    - Set expiration when creating a short URL.
    - Soft-delete a URL (mark as deleted without removing from DB).
    - Permanently delete if needed (admin-only).

##### Frontend Experience:

- Show a clear message like “This link has expired” or “This URL is no longer available.”
- Optionally, offer the user a way to regenerate or restore the link if authenticated.

This approach ensures graceful handling of expired or deleted URLs while maintaining system integrity and user
experience.

#### How would you extend the system to support QR code generation?

This feature would be useful for sharing links offline, in print, or on physical products.

To support QR code generation, I would enhance the backend API to generate a QR code for each shortened URL. When a user
submits a long URL, the backend would return both the short URL and a QR code image.

##### Backend Implementation:

- Use a library like `qrcode` (Node.js), `qrcode-generator` (Python), or `ZXing` (Java) to generate QR codes.
- Encode the short URL into the QR code.
- Return the QR code as a base64-encoded image or a downloadable file.

##### API Response Example:

```json
{
  "shortUrl": "https://sho.rt/abc123",
  "qrCode": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."
}
```

##### Frontend Integration:

- Display the QR code image alongside the short URL.
- Allow users to download or copy the QR code.
- Optionally, provide customization options like size, color, and logo overlay

##### Storage and Caching:

- Store QR codes temporarily or regenerate them on demand.
- Use CDN or object storage (e.g., AWS S3) for hosting if persistent access is needed.
