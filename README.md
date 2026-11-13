# 🛡️ CyberSentinel – AI-Powered Cyber Threat Detection and Incident Analysis Platform

An AI-powered cybersecurity platform that uses Machine Learning to detect and classify network threats from network-flow data. It provides threat risk assessment, attack intelligence, and a web-based dashboard for analyzing detection results.

**Project Type:** MCA Minor Project  
**Dataset:** CICIDS2017  
**Machine Learning Model:** Random Forest Classifier  
**Backend:** Python, FastAPI  
**Frontend:** React.js, Vite  
**Database:** MongoDB Atlas  
**Status:** Under Development

---

## 📌 Table of Contents

1. [About the Project](#-about-the-project)
2. [Problem Statement](#-problem-statement)
3. [Objectives](#-objectives)
4. [Key Features](#-key-features)
5. [Technology Stack](#-technology-stack)
6. [System Architecture](#-system-architecture)
7. [Dataset and Machine Learning](#-dataset-and-machine-learning)
8. [Model Performance](#-model-performance)
9. [Project Structure](#-project-structure)
10. [Installation and Setup](#-installation-and-setup)
11. [Running the Project](#-running-the-project)
12. [API Endpoints](#-api-endpoints)
13. [Testing](#-testing)
14. [Team Git Workflow](#-team-git-workflow)
15. [Project Limitations](#-project-limitations)
16. [Future Improvements](#-future-improvements)
17. [Project Team](#-project-team)

---

## 🔍 About the Project

CyberSentinel is a Machine Learning-based cybersecurity threat detection and incident analysis platform.

The system analyzes network-flow data and predicts whether the traffic is benign or belongs to a known attack category.

It uses a trained Random Forest model to classify network traffic and assigns a preliminary risk score and risk level to each prediction.

The platform also provides attack intelligence information, including:

- Attack descriptions
- Potential security impact
- Common indicators
- Recommended mitigation measures
- Risk assessment

The results are displayed through an interactive React dashboard.

The current implementation processes uploaded CSV files containing network-flow features. It does not capture live network traffic.

## 🎯 Problem Statement

Network security monitoring can generate large amounts of technical information that may be difficult to understand and analyze.

The goal of CyberSentinel is to develop a platform that can:

1. Analyze network-flow data.
2. Identify suspicious network activity.
3. Classify known network attacks.
4. Estimate the risk level of detected threats.
5. Provide understandable attack information.
6. Store historical detection records.
7. Display detection results through a web dashboard.

## 🎯 Project Objectives

- Develop a Machine Learning-based threat detection system.
- Process and analyze network-flow datasets.
- Train a multi-class classification model.
- Detect multiple categories of network attacks.
- Display prediction confidence.
- Assign preliminary threat risk levels.
- Store detection history in MongoDB.
- Develop an interactive web dashboard.
- Provide attack descriptions and mitigation recommendations.

## ⭐ Key Features

### 1. Machine Learning Threat Detection

- Random Forest classification.
- Multi-class attack prediction.
- Network-flow CSV processing.
- Prediction confidence calculation.

### 2. Risk Assessment

- Risk score calculation.
- Low, Medium, High and Critical risk levels.
- Attack-category-based risk assessment.

### 3. Threat Intelligence

- Attack descriptions.
- Potential impacts.
- Common attack indicators.
- Mitigation recommendations.

### 4. Web Dashboard

- Overview dashboard.
- CSV file upload.
- Threat detection results.
- Attack distribution.
- Detection history.
- Detailed threat reports.

### 5. Database Integration

- MongoDB Atlas integration.
- Detection history storage.
- Historical prediction retrieval.

## 🛠️ Technology Stack

| Category             | Technologies         |
| -------------------- | -------------------- |
| Programming Language | Python, JavaScript   |
| Machine Learning     | Scikit-learn         |
| Data Processing      | Pandas, NumPy        |
| Model Storage        | Joblib               |
| Backend              | FastAPI, Uvicorn     |
| Frontend             | React.js, Vite       |
| Styling              | CSS                  |
| Database             | MongoDB Atlas        |
| API Communication    | REST API             |
| Development Tools    | Git, GitHub, VS Code |

## 🏗️ System Architecture

```text
              Network Flow CSV
                     |
                     v
              CSV File Upload
                     |
                     v
              React Dashboard
                     |
                     v
               FastAPI Backend
                     |
                     v
             Data Preprocessing
                     |
                     v
           Trained Random Forest
                     |
                     v
             Threat Prediction
                     |
             +-------+-------+
             |               |
             v               v
       Attack Type       Confidence
             |
             v
         Risk Scoring
             |
             v
       Threat Intelligence
             |
             v
       Detection Results
             |
        +----+-----+
        |          |
        v          v
    Dashboard   MongoDB Atlas
                  History
```

## 📊 Dataset and Machine Learning

The project uses the CICIDS2017 dataset for training and evaluating the Machine Learning model.

CICIDS2017 contains benign and malicious network traffic represented through network-flow features.

### Dataset Details

- Original CSV files: 8
- Network-flow features: 78
- Target column: `Label`
- Prepared dataset: approximately 149,201 rows.

### Data Preprocessing

The preprocessing pipeline includes:

1. Reading the original CSV files.
2. Combining the network traffic records.
3. Sampling up to 10,000 records per attack category.
4. Handling missing and infinite values.
5. Removing invalid records.
6. Shuffling the prepared dataset.

### Machine Learning Algorithm

The project uses the Random Forest Classifier.

Model configuration:

```python
RandomForestClassifier(
    n_estimators=150,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced_subsample",
    max_features="sqrt"
)
```

The dataset is divided into training and testing sets using an 80:20 stratified split.

### Attack Categories

The model supports categories such as:

- BENIGN
- DDoS
- DoS Hulk
- DoS GoldenEye
- DoS slowloris
- DoS Slowhttptest
- PortScan
- Bot
- FTP-Patator
- SSH-Patator
- Web Attack Brute Force
- Web Attack XSS
- SQL Injection
- Heartbleed
- Infiltration

## 📈 Model Performance

Current evaluation results:

| Metric            | Result |
| ----------------- | -----: |
| Accuracy          | 99.23% |
| Macro F1-score    |   0.91 |
| Weighted F1-score |   0.99 |

Some minority attack categories have limited training and testing examples.

Examples of class-level F1-scores:

| Attack Category          | F1-score |
| ------------------------ | -------: |
| Web Attack Brute Force   |     0.76 |
| Web Attack SQL Injection |     0.57 |
| Web Attack XSS           |     0.39 |

These results are based on a held-out split of the prepared CICIDS2017 dataset. They should not be interpreted as guaranteed real-world detection accuracy.

## 💾 Trained Model Files

The following files are required to run the existing trained model:

```text
models/
├── random_forest_model.pkl
├── label_encoder.pkl
└── feature_names.pkl
```

- `random_forest_model.pkl`: Trained Random Forest model.
- `label_encoder.pkl`: Encoded attack-category mapping.
- `feature_names.pkl`: Required input feature names.

**Important:** These model files must be included in the GitHub repository. The original dataset is not required to run predictions with the already-trained model.

## 📁 Project Structure

```text
AI-Cyber-Threat-Detection/
│
├── backend/
│   └── main.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── index.html
│
├── ml/
│   ├── inspect_dataset.py
│   ├── prepare_dataset.py
│   ├── train_model.py
│   ├── test_model.py
│   └── create_test_samples.py
│
├── models/
│   ├── random_forest_model.pkl
│   ├── label_encoder.pkl
│   └── feature_names.pkl
│
├── test_data/
│
├── dataset/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

The dataset directory may be empty on a teammate's computer. The trained model files must be available.

## 💻 Installation and Setup

### Prerequisites

Install the following software:

- Python 3
- Node.js and npm
- Git
- Visual Studio Code

### Step 1: Clone the Repository

```bash
git clone https://github.com/Kritika011/AI-Cyber-Threat-Detection.git
```

Move into the project directory:

```bash
cd AI-Cyber-Threat-Detection
```

For a private repository, the GitHub owner must first invite you as a collaborator.

### Step 2: Create a Python Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate again:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root.

Use `.env.example` as a reference.

Add the required MongoDB connection string:

```env
MONGO_URI=your_mongodb_connection_string
```

Use your own valid database credentials. Never commit the real `.env` file to GitHub.

The MongoDB Atlas cluster must also allow connections from the computer's IP address.

### Step 5: Install Frontend Dependencies

Open a second terminal:

```bash
cd frontend
npm install
```

## 🚀 Running the Project

The backend and frontend must run in separate terminals.

### Terminal 1: Start the Backend

From the main project directory:

```bash
python -m uvicorn backend.main:app --reload
```

Backend URL:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs

### Terminal 2: Start the Frontend

```bash
cd frontend
npm run dev
```

Frontend URL:

http://localhost:5173

Open the frontend URL in your browser to access CyberSentinel.

## 🔗 API Endpoints

The backend currently provides the following endpoints:

| Method | Endpoint   | Purpose                        |
| ------ | ---------- | ------------------------------ |
| GET    | `/`        | Check API availability         |
| GET    | `/health`  | Check backend and model health |
| POST   | `/predict` | Upload CSV and predict threats |
| GET    | `/history` | Retrieve detection history     |

### POST /predict

Accepts a CSV file containing the required network-flow features.

The response includes information such as:

- Uploaded filename
- Total number of network flows
- Predicted attack category
- Prediction confidence
- Risk score
- Risk level
- Risk explanation

### GET /history

Retrieves previously stored detection records from MongoDB.

Example:

```text
http://127.0.0.1:8000/history?limit=20
```

## 🧪 Testing

You can test the backend through FastAPI Swagger documentation.

1. Start the backend.
2. Open http://127.0.0.1:8000/docs.
3. Find the `POST /predict` endpoint.
4. Click **Try it out**.
5. Upload a CSV file with the required network-flow features.
6. Click **Execute**.
7. Check the prediction response.

The frontend also supports uploading CSV files and viewing the results through the dashboard.

## 👥 Team Git Workflow

All team members should work using the same GitHub repository.

### 1. Clone the Repository

```bash
git clone https://github.com/Kritika011/AI-Cyber-Threat-Detection.git
cd AI-Cyber-Threat-Detection
```

### 2. Create Your Own Branch

```bash
git checkout -b your-name
```

Example:

```bash
git checkout -b sudipta
```

### 3. Update Your Local Repository

Before starting new work:

```bash
git checkout main
git pull origin main
git checkout your-name
```

### 4. Save Your Changes

```bash
git add .
git commit -m "Describe your changes"
```

### 5. Push Your Branch

```bash
git push -u origin your-name
```

### 6. Create a Pull Request

Open GitHub and create a Pull Request from your branch into `main`.

Team members should review changes before merging them into the main branch.

**Avoid directly pushing unfinished changes to `main`.**

## ⚠️ Project Limitations

1. **Dataset Dependence:** The model is trained using CICIDS2017 and may not generalize to all real-world network traffic.
2. **Class Imbalance:** Some attack categories have very few examples.
3. **Prediction Confidence:** Model confidence is not necessarily a calibrated probability of a real-world attack.
4. **Risk Scoring:** Current risk classification uses preliminary rules and requires further validation.
5. **No Live Monitoring:** The current system analyzes uploaded CSV network-flow data. It does not capture live network packets.
6. **Academic Prototype:** The platform is not a production-grade intrusion detection system.

## 🔮 Future Improvements

- Google Gemini API integration for AI-assisted threat explanations.
- Improved threat risk assessment.
- Better handling of minority attack categories.
- Independent dataset validation.
- Real-time network-flow monitoring.
- Advanced threat intelligence.
- SHAP-based model explainability.
- User authentication and role-based access.
- Advanced analytics and reporting.
- Automated security alerts.
- Cloud deployment.
- Docker containerization.

## 👩‍💻 Project Team

**MCA Minor Project Team**

| Team Member      | Responsibility                           |
| ---------------- | ---------------------------------------- |
| Kritika Pramanik | Machine Learning and Project Integration |
| Sudipta Biswas   | Backend and Cybersecurity                |
| Subhajoy Paul    | Database and Backend                     |
| Sumit Singh      | Frontend and Integration                 |

**Project Guide:** Tapan Kumar Chakraborty

## 📌 Disclaimer

CyberSentinel is an academic cybersecurity research prototype intended for educational, testing, and research purposes.

It should not be used as the sole security mechanism for protecting production infrastructure.

## 📄 License

All rights are reserved by the project authors unless otherwise stated.
