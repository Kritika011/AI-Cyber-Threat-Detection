# 🛡️ AI-Powered Cybersecurity Threat Detection and Incident Analysis System

An AI-powered cybersecurity system that uses Machine Learning to detect and classify network security threats from network-flow data and Generative AI to provide human-readable threat explanations and mitigation recommendations.

> **Project Status:** 🚧 In Development  
> **Project Type:** MCA Minor Project  
> **Dataset:** CICIDS2017  
> **ML Model:** Random Forest  
> **Backend:** FastAPI  
> **Frontend:** React.js (Planned)  
> **Generative AI:** Google Gemini API (Planned)  
> **Database:** MySQL (Planned)

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Problem Statement](#-problem-statement)
- [Project Objectives](#-project-objectives)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Technology Stack](#-technology-stack)
- [Dataset](#-dataset)
- [Machine Learning](#-machine-learning)
- [Current ML Results](#-current-ml-results)
- [Backend API](#-backend-api)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Running the Project](#-running-the-project)
- [Testing the API](#-testing-the-api)
- [Team Git Workflow](#-team-git-workflow)
- [Development Roadmap](#-development-roadmap)
- [Important Notes](#-important-notes)
- [Limitations](#-limitations)
- [Future Improvements](#-future-improvements)
- [Team](#-team)
- [License](#-license)

---

# 🔍 About the Project

The **AI-Powered Cybersecurity Threat Detection and Incident Analysis System** is designed to identify malicious network activity using Machine Learning.

The system analyzes network-flow features and classifies traffic into different categories such as:

- BENIGN
- DDoS
- DoS Hulk
- DoS GoldenEye
- DoS Slowhttptest
- DoS slowloris
- PortScan
- Bot
- FTP-Patator
- SSH-Patator
- Web Attacks
- Infiltration
- Heartbleed

The system is designed to eventually combine Machine Learning with Generative AI.

The Machine Learning model identifies the type of threat, while the Generative AI component will explain:

- What the detected attack means
- Why it may be dangerous
- Possible impact
- Recommended mitigation steps
- Security response suggestions

---

# 🎯 Problem Statement

Traditional cybersecurity monitoring systems can generate large amounts of network security alerts that can be difficult to interpret.

The goal of this project is to build a system that can:

1. Analyze network-flow data.
2. Detect suspicious network activity.
3. Classify the detected attack.
4. Assign a risk level.
5. Provide an understandable explanation of the detected threat.
6. Store historical detection results.
7. Display the results through a web-based dashboard.

The current implementation focuses on the Machine Learning detection pipeline and FastAPI backend.

---

# 🎯 Project Objectives

### Primary Objectives

- Build a Machine Learning-based cybersecurity threat detection system.
- Process network-flow data using Python.
- Train a classification model using CICIDS2017.
- Detect multiple categories of network attacks.
- Provide prediction confidence.
- Assign a preliminary risk level.
- Provide a REST API for threat detection.

### Planned Objectives

- Integrate Google Gemini for AI-based threat explanations.
- Store detection history using MySQL.
- Build a React dashboard.
- Display statistics and visualizations.
- Provide detailed threat analysis.
- Support CSV upload through the web interface.

---

# ⭐ Key Features

## Currently Implemented

- CICIDS2017 dataset processing
- Multi-class network attack classification
- Data cleaning
- Class balancing through sampling
- Random Forest model training
- Model evaluation
- Model serialization
- FastAPI backend
- CSV upload API
- Threat prediction API
- Prediction confidence
- Preliminary risk classification
- Swagger API documentation

## Planned

- Gemini AI threat explanation
- MySQL database
- Threat history
- React dashboard
- Authentication
- Charts and statistics
- Detailed threat analysis page
- Improved risk scoring
- Model comparison
- Production deployment

---

# 🏗️ System Architecture

Current architecture:

````text
             CICIDS2017 Dataset
                     │
                     ▼
             Data Preprocessing
                     │
                     ▼
              Dataset Sampling
                     │
                     ▼
             Random Forest Model
                     │
                     ▼
              Saved ML Model
                     │
                     ▼
              FastAPI Backend
                     │
                     ▼
               CSV Upload
                     │
                     ▼
             Threat Prediction
                     │
              ┌──────┴──────┐
              ▼             ▼
          Prediction     Confidence
              │
              ▼
          Risk Level
                            ┌──────────────────┐
                  │   User / Admin   │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ React Dashboard  │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │   FastAPI API    │
                  └────────┬─────────┘
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
          ┌──────────────┐    ┌──────────────┐
          │ ML Detection │    │ MySQL        │
          │ RandomForest │    │ Database     │
          └──────┬───────┘    └──────────────┘
                 │
                 ▼
          ┌──────────────┐
          │ Risk Scoring │
          └──────┬───────┘
                 │
                 ▼
          ┌──────────────┐
          │ Gemini AI    │
          │ Explanation  │
          └──────┬───────┘
                 │
                 ▼
          Threat Analysis


# 🛠️ Technology Stack
Machine Learning
Python
Pandas
NumPy
Scikit-learn
Joblib
Backend
Python
FastAPI
Uvicorn
Python Multipart
Frontend

Planned:

React.js
Tailwind CSS
Recharts / Chart.js
Database

Planned:

MySQL
Generative AI

Planned:

Google Gemini API
Development Tools
Git
GitHub
VS Code
PowerShell
📊 Dataset

This project uses the CICIDS2017 dataset.

CICIDS2017 contains network traffic representing both benign and malicious activity.

The dataset contains network-flow features that can be used for Machine Learning-based intrusion detection.

The downloaded dataset contains 8 CSV files:

Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
Friday-WorkingHours-Morning.pcap_ISCX.csv
Monday-WorkingHours.pcap_ISCX.csv
Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
Tuesday-WorkingHours.pcap_ISCX.csv
Wednesday-workingHours.pcap_ISCX.csv

Each file contains approximately 79 columns, including the target Label column.

🧹 Data Preprocessing

The original dataset is large, so the project currently creates a smaller balanced working dataset.

The preprocessing pipeline:

Original CICIDS2017 CSV files
          │
          ▼
Read CSV files
          │
          ▼
Combine attack classes
          │
          ▼
Sample up to 10,000 rows per label
          │
          ▼
Remove invalid/missing values
          │
          ▼
Shuffle dataset
          │
          ▼
cicids_balanced.csv

The current prepared dataset contains:

Rows: approximately 149,201
Columns: 79
Features: 78
Target: Label
🤖 Machine Learning Model

The current model is:

Random Forest Classifier

Configuration:

RandomForestClassifier(
    n_estimators=150,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced_subsample",
    max_features="sqrt"
)

The target column is:

Label

The labels are converted into numerical values using:

LabelEncoder

The dataset is split using an 80/20 stratified train/test split.

📈 Current ML Results

The current model achieved approximately:

Accuracy: 99.23%

Macro F1:    0.91
Weighted F1: 0.99

Some classes have significantly fewer examples than others.

Therefore, accuracy alone should not be treated as sufficient evidence of model quality.

The current evaluation shows particularly weaker performance on some rare Web Attack categories.

For example, the current test results included approximately:

Web Attack Brute Force   F1 ≈ 0.76
Web Attack SQL Injection F1 ≈ 0.57
Web Attack XSS           F1 ≈ 0.39

Some rare classes also have very small numbers of examples.

For example:

Heartbleed       11 examples
Infiltration     36 examples
SQL Injection    21 examples

Therefore, these results require further evaluation before making strong claims about real-world detection performance.

💾 Saved Machine Learning Files

After training, the following files are generated:

models/
├── random_forest_model.pkl
├── label_encoder.pkl
└── feature_names.pkl
random_forest_model.pkl

Contains the trained Random Forest model.

label_encoder.pkl

Contains the mapping between numerical class IDs and attack labels.

feature_names.pkl

Contains the feature names required by the model.

🚀 Backend API

The current backend uses FastAPI.

Main backend file:

backend/main.py

The backend runs on:

http://127.0.0.1:8000
🔗 API Endpoints
GET /

Checks whether the API is running.

Example response:

{
  "message": "AI Cyber Threat Detection API is running"
}
GET /health

Checks backend and model status.

Example:

{
  "status": "healthy",
  "model": "Random Forest"
}
POST /predict

Uploads a CSV file and performs threat detection.

Example request:

POST /predict

Input:

CSV file containing the required network-flow features

Example response:

{
  "filename": "test_sample.csv",
  "total_flows": 10,
  "results": [
    {
      "prediction": "BENIGN",
      "confidence": 100,
      "risk": "Low"
    },
    {
      "prediction": "DoS Hulk",
      "confidence": 100,
      "risk": "High"
    }
  ]
}
⚠️ Current Risk Classification

The current implementation uses a preliminary rule-based risk system.

BENIGN
   ↓
Low

Non-BENIGN + confidence >= 90%
   ↓
High

Non-BENIGN + confidence >= 70%
   ↓
Medium

Other
   ↓
Low

This is a temporary implementation.

The risk-scoring system will be improved later by considering:

Attack type
Model confidence
Attack severity
Frequency
Number of affected flows
Historical activity
Other security indicators
📁 Project Structure

Current project structure:

AI-Cyber-Threat-Detection/
│
├── backend/
│   └── main.py
│
├── frontend/
│
├── ml/
│   ├── inspect_dataset.py
│   ├── prepare_dataset.py
│   ├── train_model.py
│   └── test_model.py
│
├── dataset/
│   ├── MachineLearningCVE/
│   ├── cicids_balanced.csv
│   └── test_sample.csv
│
├── models/
│   ├── random_forest_model.pkl
│   ├── label_encoder.pkl
│   └── feature_names.pkl
│
├── .gitignore
├── requirements.txt
└── README.md

Dataset files and trained model files are excluded from GitHub using .gitignore because of their size and reproducibility considerations.

💻 Installation
1. Clone the Repository
git clone YOUR_GITHUB_REPOSITORY_URL

Example:

git clone https://github.com/YOUR_USERNAME/AI-Cyber-Threat-Detection.git

Enter the project:

cd AI-Cyber-Threat-Detection
🐍 Python Virtual Environment

Create a virtual environment:

python -m venv venv

Activate it on Windows PowerShell:

.\venv\Scripts\Activate.ps1

If PowerShell blocks activation, you can use:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Then activate again:

.\venv\Scripts\Activate.ps1
📦 Install Dependencies

Install the required packages:

pip install -r requirements.txt

Current core dependencies include:

pandas
numpy
scikit-learn
joblib
fastapi
uvicorn
python-multipart
📥 Dataset Setup

The CICIDS2017 dataset is not stored directly in this GitHub repository.

Download the dataset separately and place the extracted files under:

dataset/MachineLearningCVE/

The expected structure is:

dataset/
└── MachineLearningCVE/
    ├── Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
    ├── Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
    ├── Friday-WorkingHours-Morning.pcap_ISCX.csv
    ├── Monday-WorkingHours.pcap_ISCX.csv
    ├── Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
    ├── Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
    ├── Tuesday-WorkingHours.pcap_ISCX.csv
    └── Wednesday-workingHours.pcap_ISCX.csv
🧪 Prepare the Dataset

From the project root:

python ml/inspect_dataset.py

This checks the dataset files and their structure.

Then run:

python ml/prepare_dataset.py

This creates:

dataset/cicids_balanced.csv
🏋️ Train the Model

Run:

python ml/train_model.py

This trains the Random Forest model and generates:

models/random_forest_model.pkl
models/label_encoder.pkl
models/feature_names.pkl
🧪 Test the Model

Run:

python ml/test_model.py

This performs a basic prediction test using the saved model.

🚀 Run the FastAPI Backend

From the project root:

python -m uvicorn backend.main:app --reload

The API should start at:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs
🧪 Testing the Prediction API

A small sample file can be created from the prepared dataset:

python -c "import pandas as pd; df=pd.read_csv('dataset/cicids_balanced.csv', nrows=10); df.to_csv('dataset/test_sample.csv', index=False); print('Created dataset/test_sample.csv with', len(df), 'rows')"

Then:

Open /docs.
Find POST /predict.
Click Try it out.
Upload dataset/test_sample.csv.
Click Execute.

The API should return:

Filename
Number of network flows
Predicted attack
Confidence
Risk level
🔐 Environment Variables

Future API keys and secrets must never be committed to GitHub.

For example, when Gemini is added:

.env

will contain:

GEMINI_API_KEY=your_api_key_here

The .env file must remain in .gitignore.

Never write API keys directly inside Python or React source code.

👥 Team Git Workflow

This project is developed collaboratively using GitHub.

Each team member should work on their own branch.

Example:

main
│
├── kritika
├── data-ml
├── backend
└── frontend
Clone the Project
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Cyber-Threat-Detection
Create a Branch

Example:

git checkout -b your-name

For example:

git checkout -b kritika
Before Starting Work

Always update your local repository:

git checkout main
git pull origin main

Then return to your branch:

git checkout your-name
Save Changes

Check changes:

git status

Add files:

git add .

Commit:

git commit -m "Describe your changes"

Push:

git push -u origin your-name
🔀 Pull Request Workflow

After finishing a feature:

Your Branch
     ↓
git push
     ↓
GitHub
     ↓
Pull Request
     ↓
Code Review
     ↓
main

Do not directly push experimental or unfinished work to main.

🗺️ Development Roadmap
Phase 1 — Dataset and ML
Status: ✅ Completed
 Download CICIDS2017
 Inspect dataset
 Identify target column
 Clean missing/infinite values
 Prepare balanced working dataset
 Train Random Forest
 Evaluate model
 Save model
 Test prediction pipeline
Phase 2 — FastAPI Backend
Status: ✅ Partially Completed
 Create FastAPI application
 / endpoint
 /health endpoint
 /predict endpoint
 CSV upload
 ML prediction
 Confidence calculation
 Basic risk classification
 Swagger API documentation
Remaining
 Better error handling
 Improved risk scoring
 Structured threat response
 Gemini integration
 Database integration
Phase 3 — Generative AI
Status: ⏳ Planned

Integrate Google Gemini API.

Expected workflow:

ML Prediction
      ↓
Attack Type
      ↓
Gemini API
      ↓
Threat Explanation
      ↓
Impact
      ↓
Mitigation
      ↓
Security Recommendations

Example:

Detected Threat:
DoS Hulk

Risk:
High

AI Explanation:
...

Potential Impact:
...

Recommended Mitigation:
...
Phase 4 — Database
Status: ⏳ Planned

MySQL will store:

User information
Detection history
Uploaded file information
Predictions
Confidence
Risk level
AI explanations
Timestamps

Possible database tables:

users
detections
threat_analysis
Phase 5 — React Dashboard
Status: ⏳ Planned

Planned pages:

Login
   │
   ▼
Dashboard
   │
   ├── Threat Detection
   │
   ├── Threat History
   │
   └── Threat Details

Dashboard will display:

Total scans
Total threats
Benign traffic
High-risk threats
Attack distribution
Recent detections
Threat details
AI explanations
Phase 6 — Authentication
Status: ⏳ Planned

Planned authentication:

Login
Registration
JWT authentication
Protected API routes
User-specific detection history
🧪 Testing Plan

The project will eventually include:

Machine Learning Testing
Accuracy
Precision
Recall
F1-score
Confusion matrix
Per-class performance
Cross-validation
Independent test data
Backend Testing
API availability
File upload validation
Missing feature detection
Invalid CSV handling
Model prediction
API response format
Frontend Testing
Login
CSV upload
Dashboard rendering
API errors
Threat details
History
Integration Testing
React
 ↓
FastAPI
 ↓
ML Model
 ↓
Risk Scoring
 ↓
Gemini
 ↓
MySQL
⚠️ Important Limitations

The current system is a research/academic prototype.

It should not currently be considered a production-grade intrusion detection system.

Important limitations include:

1. Dataset Dependence

The model is trained using CICIDS2017 and may not generalize perfectly to modern real-world network traffic.

2. Class Imbalance

Some attack classes contain very few samples.

Therefore, metrics for extremely rare classes should be interpreted carefully.

3. Current Evaluation

The current evaluation uses a train/test split from the prepared dataset.

An independent external dataset should be used for stronger validation.

4. Confidence

A Random Forest prediction probability should not automatically be interpreted as a calibrated probability of a real-world attack.

5. Risk Scoring

The current risk score is preliminary and will be improved.

6. No Real-Time Network Monitoring

The current system analyzes uploaded CSV network-flow data.

It does not currently capture live network traffic.

🔮 Future Improvements

Potential future improvements include:

Real-time traffic monitoring
Streaming network-flow analysis
XGBoost model comparison
Neural network comparison
Model explainability
SHAP-based explanations
Improved class imbalance handling
Independent dataset validation
Automated incident response
Email alerts
Security notifications
Advanced risk scoring
Role-based access
Cloud deployment
Containerization using Docker
Monitoring and logging
Model retraining pipeline
📚 Research and Academic Use

This project can be used to study:

Cybersecurity
Intrusion Detection Systems
Machine Learning
Classification
Network Security
Generative AI
Threat Intelligence
REST APIs
Data Science
Human-readable security analysis

The project is intended for educational and research purposes.

👩‍💻 Team
MCA Minor Project Team
Member	Responsibility
Kritika Pramanik	Machine Learning & Project Integration
Sudipta Biswas	Backend / Cybersecurity
Subhajoy Paul	Database / Backend
Sumit Singh	Frontend / Integration

Responsibilities may change as development progresses.

📌 Current Project Status
Completed
✅ CICIDS2017 dataset setup
✅ Dataset inspection
✅ Data preprocessing
✅ Balanced working dataset
✅ Random Forest training
✅ Model evaluation
✅ Model serialization
✅ Prediction testing
✅ FastAPI backend
✅ CSV upload
✅ Threat classification
✅ Confidence calculation
✅ Basic risk scoring
✅ Swagger API
In Progress / Planned
⏳ Improved risk scoring
⏳ Gemini AI integration
⏳ MySQL database
⏳ React frontend
⏳ Dashboard
⏳ Authentication
⏳ Threat history
⏳ AI threat analysis
⏳ Full system integration
⚖️ Disclaimer

This project is an academic cybersecurity research prototype.

It is intended for educational, testing, and research purposes using publicly available network-flow data.

The system should not be used as the sole security mechanism for protecting production infrastructure.

📄 License

License information will be added after the project team decides on the appropriate license.


### One correction I'd make before you commit this

In your actual repository, **don't put the current `dataset/` contents or `.pkl` files in GitHub**. Keep them locally and let the README explain how teammates recreate them.

Also, because your project is being developed by four people, the **Git workflow section is particularly important**. Everyone should clone the same repository, create their own branch, and use Pull Requests rather than editing `main` directly.

Once you create this `README.md`, your next Git commands can be:

```powershell
git add README.md .gitignore requirements.txt
git commit -m "Add project documentation and setup instructions"
git push
````
