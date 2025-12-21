# Employee Attrition Prediction – End-to-End ML Pipeline

## Overview
Employee attrition leads to significant cost and productivity loss for organizations.  
This project implements a **production-ready, end-to-end machine learning system** to predict employee attrition, covering the **entire ML lifecycle** from data validation to deployment and monitoring.

The project follows **real-world ML engineering practices**, including experiment tracking, API deployment, containerization, and drift monitoring.

---

## 🏗️ System Architecture

→ Raw HR Data  
→ Data Cleaning & Validation  
→ Feature Engineering  
→ Preprocessing  
→ Model Training (XGBoost)  
→ Model Tracking (MLflow)  
→ FastAPI Inference Service  
→ Docker Container  
→ Monitoring & Drift Detection(Evidently AI)

---

## 📊 Dataset
- **Source**: IBM HR Analytics – Employee Attrition Dataset
- **Target**: `Attrition` (Yes / No)

---

## 🧪 ML Pipeline

### 1. Data Cleaning & Validation
- Schema validation
- Data type checks
- Missing value
- Value range checks
- Target validation

### 2. Feature Engineering
- Income normalized by tenure
- Promotion rate
- Tenure bucketing
- Composite satisfaction score
- Overtime binary flag

### 3. Preprocessing
- Missing value imputation
- One-hot encoding for categoricals
- Feature scaling for numerics
- Reusable `ColumnTransformer` pipeline

### 4. Model Training
- Algorithm: **XGBoost Classifier**
- Stratified train-test split
- Metric: **ROC-AUC**
- Model and preprocessing artifacts saved using `joblib`

### 5. Experiment Tracking
- **MLflow** used to log:
  - Hyperparameters
  - Metrics
  - Model artifacts
- Reproducible and auditable experiments

---

## 🚀 Inference Service
- Built using **FastAPI**
- REST endpoint `/predict`
- Input validation with Pydantic
- Returns attrition probability
- Uses same feature engineering & preprocessing as training

---

## 🐳 Containerization
- Dockerized FastAPI application
- Includes trained model and preprocessing artifacts
- Portable and cloud-ready

---

## 📈 Monitoring & Drift Detection
- Implemented using **Evidently AI**
- Detects input data drift post-deployment
- Generates HTML dashboard for monitoring feature stability

---

## 🛠️ Tech Stack
- **Language**: Python
- **ML**: Scikit-learn, XGBoost
- **MLOps**: MLflow, Evidently AI
- **API**: FastAPI
- **Deployment**: Docker
- **Monitoring**: Evidently AI

---

## ▶️ How to Run

### Training
```bash
python src/train.py
python src/train_model.py

API - uvicorn api.main:app --reload

Docker - docker build -t attrition-ml-api .
docker run -p 8000:8000 attrition-ml-api
