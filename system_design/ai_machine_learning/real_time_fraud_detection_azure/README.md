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

- **fraud_detection_training_pipeline_with_schedule.yml**  
  Extended pipeline with **automated retraining schedules** (weekly and daily cron triggers).  
  - Weekly full retraining  
  - Daily incremental retraining  
  - Integrates with Azure DevOps/GitHub Actions for CI/CD

- **decision_service_deployment.yaml**  
  Minimal AKS deployment manifest for the Decision service.  
  - Deploys a containerized fraud decision API  
  - Connects to Azure ML Online Endpoint for real-time scoring  
  - Exposes service via LoadBalancer for external access

- **app_insights_config.yaml**  
  Application Insights configuration for latency and performance monitoring.  
  - Collects request duration, throughput, and error rates  
  - Supports custom telemetry for ML scoring latency

- **latency_alert_rules.json**  
  Azure Monitor alert rules for latency thresholds.  [Usage guide for latency alert rules](./latency_alert_rules_usage.md) 
  - Triggers alerts if average request latency exceeds 2000 ms over a 5-minute window  
  - Routes alerts to configured action groups (email, SMS, Logic Apps)

- **model_drift_monitor.yaml**  
  Drift detection manifest for fraud detection models.  [Usage guide for model drift monitor](./model_drift_monitor_usage.md)
  - Compares live transaction features against baseline dataset  
  - Metrics: Population Stability Index (PSI), Kolmogorov-Smirnov test  
  - Alerts triggered if drift thresholds are exceeded

---

## 🧩 How These Files Fit Into the System Design

- **Training pipelines** ensure fraud detection models are continuously updated with fresh data and retrained on labeled outcomes (e.g., chargebacks, disputes).  
- **Deployment manifests** provide a scalable, low-latency API that integrates rules and ML scoring to block or challenge suspicious transactions in real time.  
- **Monitoring manifests** ensure observability of latency, throughput, and model health. They trigger alerts when performance or drift thresholds are breached.  
  - See [latency_alert_rules_usage.md](./latency_alert_rules_usage.md) for instructions on applying latency alerts.  
  - See [model_drift_monitor_usage.md](./model_drift_monitor_usage.md) for instructions on configuring drift detection.  
- Together, these assets operationalize the architecture described in `real_time_fraud_detection_azure_design.md`.

---

## 🚀 Next Steps

- Integrate case management workflows (Service Bus + Logic Apps) for analyst review.
- Add **drift-triggered retraining pipelines** that automatically launch when drift alerts fire.
- Integrate with Azure DevOps release pipelines for automatic deployment of new models after successful evaluation.
- Use approval gates (manual or automated) before promoting models to production.
- Integrate **case management workflows** (Service Bus + Logic Apps) for analyst review.
- Build dashboards in **Azure Monitor Workbooks** for unified visibility across latency, drift, and fraud metrics.

---

## 🧣 Bonus points
- prepare a GitHub Actions workflow YAML that ties this Azure ML pipeline into CI/CD, so retraining can be triggered both by schedule and by code/data changes

---
