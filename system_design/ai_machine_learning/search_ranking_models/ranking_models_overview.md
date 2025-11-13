# Search Ranking Models Overview

This document provides concise descriptions of machine learning models commonly used in search ranking systems. It serves as a central reference for understanding their strengths, use cases, and integration patterns.

---

## 🔤 BERT (Bidirectional Encoder Representations from Transformers)

BERT is a transformer-based deep learning model that understands language context by processing text bidirectionally. It is fine-tuned for search ranking tasks to score query-document pairs based on semantic relevance.

**Strengths:**
- Captures deep semantic relationships
- Excels in contextual understanding

**Use Case:**
- Re-ranking top-N search results with high precision

**Integration:**
- Typically used in the second stage of a two-stage ranking pipeline
- Deployed via Azure ML Online Endpoints or AKS

---

## 📈 LambdaMART

LambdaMART is a gradient-boosted decision tree algorithm optimized for ranking tasks. It learns to order documents based on pairwise relevance signals using labeled training data.

**Strengths:**
- Fast training and inference
- Interpretable and scalable
- Effective with engineered features

**Use Case:**
- Initial ranking of large candidate sets

**Integration:**
- Used in the first stage of ranking pipelines
- Trained using Azure ML pipelines with tabular features

---

## 📌 More Models to Add

- DSSM (Deep Structured Semantic Model)
- DLRM (Deep Learning Recommendation Model)
- BM25 (Best Matching 25)
- Transformer-based hybrid models
- Reinforcement learning-based rankers

