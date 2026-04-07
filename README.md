# 🏥 Scalable Healthcare Data Pipeline with Predictive Analytics (AWS Batch Architecture)

## 📌 Overview

This project implements an end-to-end **batch data pipeline on AWS** for healthcare analytics. It ingests patient data from multiple sources, processes and transforms it, and applies machine learning models to predict patient risk levels.

The architecture simulates real-world healthcare systems using a **data lake + ETL + ML pipeline**.

---

## 🎯 Objectives

* Build a scalable batch pipeline using AWS
* Store healthcare data in a data lake (S3)
* Perform ETL transformations
* Train ML models for patient risk prediction
* Serve predictions via API
* Visualize results in a dashboard

---

## 🏗️ Architecture

```
Data Sources → S3 (Raw) → Glue ETL → S3 (Processed) →
SageMaker → FastAPI → Dashboard
```

---

## ☁️ AWS Services Used

| Layer      | Service          | Purpose           |
| ---------- | ---------------- | ----------------- |
| Ingestion  | Amazon S3        | Store raw data    |
| Processing | AWS Glue         | ETL jobs          |
| Storage    | Amazon S3        | Data lake         |
| Query      | Amazon Athena    | SQL queries       |
| ML         | Amazon SageMaker | Model training    |
| API        | EC2 / Lambda     | Serve predictions |
| Monitoring | CloudWatch       | Logs              |

---

## 📂 Project Structure

```
healthcare-data-pipeline/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── ingestion/
│   └── upload_to_s3.py
│
├── glue_jobs/
│   └── etl_job.py
│
├── models/
│   ├── train_sagemaker.py
│   └── predict.py
│
├── api/
│   └── app.py
│
├── dashboard/
│   └── app.py
│
├── infrastructure/
│   └── terraform.tf
│
├── requirements.txt
└── README.md
```

---

## 📥 Data Sources

* Electronic Health Records (EHR)
* Patient vitals (heart rate, blood pressure)
* Lab results (CSV files)

---

## ⚙️ Pipeline Components

### 1. Batch Ingestion

* Upload CSV files to:

```
s3://healthcare-data-lake/raw/
```

---

### 2. Data Processing (Glue)

* Clean missing values
* Transform datasets
* Join multiple sources
* Output:

```
s3://healthcare-data-lake/processed/
```

---

### 3. Query Layer (Athena)

* Run SQL queries directly on S3
* Used for analytics and feature extraction

---

### 4. Machine Learning (SageMaker)

* Train models:

  * Logistic Regression
  * Random Forest
* Outputs:

  * Risk score
  * Risk category

---

### 5. API Layer

* FastAPI endpoints:

```
/predict-risk
/health
```

---

### 6. Dashboard

* Built with Streamlit
* Displays:

  * Risk scores
  * Trends
  * Alerts

---

## 🔄 Pipeline Flow

```
1. Upload data → S3 (raw)
2. Run Glue ETL
3. Store processed data → S3
4. Query via Athena
5. Train model in SageMaker
6. Serve via API
7. Visualize in dashboard
```

---

## 🚀 Getting Started

### Clone Repo

```
git clone https://github.com/your-username/healthcare-data-pipeline.git
cd healthcare-data-pipeline
```

### Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run Steps

### Upload Data

```
python ingestion/upload_to_s3.py
```

### Run ETL

* Configure and run Glue job

### Train Model

```
python models/train_sagemaker.py
```

### Run API

```
uvicorn api.app:app --reload
```

### Run Dashboard

```
streamlit run dashboard/app.py
```

---

## 📊 Example Output

* Risk Score: 0.91
* Risk Level: High
* Alert: Immediate attention required

---

## 🔒 Security (Simulated)

* Remove PII data
* IAM roles for access control
* Secure S3 bucket policies

---

## 📈 Future Improvements

* Add streaming (Kinesis)
* Feature store integration
* CI/CD pipeline
* Model monitoring
* API Gateway + Lambda deployment

---

## 📦 Deployment

* Terraform / CloudFormation
* Docker containers
* AWS ECS / EKS

---

## 📜 License

MIT License

---

## 👨‍💻 Author

https://github.com/lasitab-bhatt
