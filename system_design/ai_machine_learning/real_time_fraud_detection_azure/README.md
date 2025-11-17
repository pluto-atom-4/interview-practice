# 🛡️ Real-Time Fraud Detection System (Azure)

This folder contains companion assets for the **Real-Time Fraud Detection System** design.  
It includes training pipeline definitions, deployment manifests, and supporting documentation.

---

## 📂 Contents

- **fraud_detection_training_pipeline.yml**  
  Azure ML pipeline definition for training and evaluating fraud detection models.  
  - Preprocessing raw transaction data  
  - Feature engineering (velocity, device, graph features)  
  - Model training (GBDT, Transformers, Graph models)  
  - Evaluation (ROC-AUC, PR-AUC, F1)  
  - Model registration and deployment

- **decision_service_deployment.yaml**  
  Minimal AKS deployment manifest for the Decision service.  
  - Deploys a containerized fraud decision API  
  - Connects to Azure ML Online Endpoint for real-time scoring  
  - Exposes service via LoadBalancer for external access

---

## 🧩 How These Files Fit Into the System Design

- The **training pipeline** ensures fraud detection models are continuously updated with fresh data and retrained on labeled outcomes (e.g., chargebacks, disputes).  
- The **decision service deployment** provides a scalable, low-latency API that integrates rules and ML scoring to block or challenge suspicious transactions in real time.  
- Together, they operationalize the architecture described in `real_time_fraud_detection_azure_design.md`.

---

## 🚀 Next Steps

- Add monitoring manifests (Azure Monitor, Application Insights) for latency and drift detection.  
- Integrate case management workflows (Service Bus + Logic Apps) for analyst review.

---
