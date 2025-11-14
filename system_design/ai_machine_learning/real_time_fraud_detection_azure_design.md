# 🛡️ System design: Real-time fraud detection system with Azure


## 🧠 Overview

Real-time fraud detection identifies and blocks suspicious activity (e.g., payments, logins, account changes) in 
milliseconds while maintaining high precision and minimizing user friction. This design combines streaming ingestion, 
low-latency inference, rules, and ML models with continuous learning loops and robust MLOps on Azure.

--- 

## 🎯 Goals

* Low-latency decisions
* High precision/recall
* Scalable and resilient
* Continuous learning
* Governance-first

---

## 🏗️ Azure-based Architecture

```text
+----------------------+        +-----------------------+        +------------------------+
| Client apps / APIs   | --->   | Azure API Management  | --->   | Decision service (AKS) |
| (Web, Mobile, POS)   |        | (throttling, auth)    |        | w/ Rules + ML scoring  |
+----------------------+        +-----------------------+        +------------------------+
          |                                                          |             |
          v                                                          v             v
+----------------------+     +---------------------------+     +------------------------+
| Event ingestion      | --> | Stream processing (ASA or| --> | Features & cache (Redis|
| (Event Hubs / Kafka) |     | Functions/Databricks)    |     | + Azure Feature Store) |
+----------------------+     +---------------------------+     +------------------------+
          |                                                          |
          v                                                          v
+----------------------+     +---------------------------+     +------------------------+
| Transaction store    |     | Models (Azure ML Online  |     | Case mgmt & alerts     |
| (Cosmos DB / SQL DB) |     | Endpoints / AKS)         |     | (Service Bus + Logic   |
+----------------------+     +---------------------------+     | Apps / Sentinel)       |
                                                               +------------------------+
          |
          v
+----------------------+
| Data lake & warehouse|
| (ADLS + Synapse)     |
+----------------------+
          |
          v
+----------------------+
| Training pipelines   |
| (Azure ML Pipelines) |
+----------------------+

```

## 🧩 Components

* Decision service (AKS / App Service)
* Event ingestion (Event Hubs / Kafka)
* Stream processing (Azure Stream Analytics / Functions / Databricks)
* Feature store & cache (Azure Feature Store + Redis)
* Models (Azure ML Online Endpoints / AKS)
* Data stores (Cosmos DB / SQL)
* Data lake & warehouse (ADLS + Synapse)
* Case management & alerts (Service Bus + Logic Apps + Sentinel)
* Observability (Azure Monitor + Application Insights)

---

## 🧪 Models and Features

### **Feature categories**:

* Velocity features
* Device & network signals
* User behavior sequences
* Graph features
* Merchant/context features

### **Model options**:
 
| Model type              | Strengths              | Use cases            |
|-------------------------|------------------------|----------------------|
| Gradient boosted trees  | Robust, interpretable  | Primary risk scoring |
| Sequence transformers   | Temporal patterns      | Account takeover     |
| Graph embeddings        | Collusion detection    | Synthetic identity   |
| Autoencoders            | Unsupervised anomalies | Cold-start entities  |

---


## 🏋️ Training Pipelines on Azure

* Data ingestion & labeling
* Preprocessing
* Model training
* Evaluation
* Registration & deployment
* Monitoring & retraining

---

## ⚡ Real-time Decisioning Flow

1. Receive transaction
2. Assemble context
3. Apply rules
4. Score with ML
5. Decide action
6. Log and emit events
7. Feedback loop

---

## 🌍 Scalability, Reliability, and Security

* Performance
* Resilience
* Security & governance

---

## 📊 Evaluation, Explainability, and Operations

* Continuous evaluation
* Explainability
* Operations

---