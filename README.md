# 🏥 PharmaGuard - Pharmacogenomic Risk Prediction System (RIFT2026)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Node 16+](https://img.shields.io/badge/Node-16%2B-green)](https://nodejs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18.2%2B-61DAFB?logo=react)](https://react.dev/)

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation & Setup](#installation--setup)
5. [Configuration](#configuration)
6. [Running the Application](#running-the-application)
7. [API Documentation](#api-documentation)
8. [Architecture](#architecture)
9. [Technology Stack](#technology-stack)
10. [Project Structure](#project-structure)
11. [Development Guide](#development-guide)
12. [Deployment](#deployment)
    - [Frontend Deployment (Netlify)](#frontend-deployment-netlify)
    - [Backend Deployment Options](#backend-deployment-options)
    - [Full-Stack Deployment](#full-stack-deployment)
13. [Troubleshooting](#troubleshooting)
14. [Contributing](#contributing)
15. [Documentation](#documentation)
16. [License](#license)

---

## 📖 Project Overview

**PharmaGuard** is a comprehensive web-based pharmacogenomic analysis platform that predicts drug safety risks based on patient genetic profiles. The system integrates genomic data (VCF files), drug information, and clinical history to provide evidence-based risk assessments, drug interaction detection, and AI-generated clinical recommendations.

### Key Features:

- 🧬 Genetic variant analysis from VCF files
- 💊 Risk assessment for 6 commonly prescribed medications
- 🔬 Pharmacogenomic phenotype calculation
- 💉 Drug-drug interaction detection
- 🤖 AI-powered clinical explanations (Google Gemini API)
- 📊 Comprehensive data visualization and reporting
- 📥 JSON export and data sharing capabilities
- 📱 Responsive, modern web interface

### Value Proposition:

- **Reduce adverse drug reactions** through personalized pharmacogenomic analysis
- **Enable precision medicine** with evidence-based medication selection
- **Improve patient outcomes** with data-driven clinical decisions
- **Support healthcare providers** with actionable clinical recommendations

---

## ✨ Features

### Core Functionality

✅ **VCF File Upload & Validation**

- Drag & drop file upload
- Format validation and error reporting
- Support for files up to 50MB

✅ **Drug Selection & Analysis**

- 6 supported medications (Warfarin, Clopidogrel, Metoprolol, Simvastatin, Sertraline, Codeine)
- Multi-select drug analyzer
- Sample data for demonstration

✅ **Pharmacogenomic Analysis**

- Gene identification and variant detection
- Phenotype mapping (PM, IM, NM, UM)
- Star allele assignment
- Metabolizer status calculation

✅ **Risk Stratification**

- 4-tier risk levels (LOW → MODERATE → HIGH → CRITICAL)
- Risk percentage scoring (0-100%)
- Severity classification
- Evidence-based reasoning

✅ **Clinical Decision Support**

- Drug-drug interaction detection
- Clinical risk modifiers based on patient history
- Dosing recommendations
- Alternative drug suggestions

✅ **AI-Generated Explanations**

- Google Gemini API integration
- Natural language variant interpretation
- Patient-friendly clinical summaries

✅ **Comprehensive Reporting**

- Summary dashboard with quick metrics
- Gene analysis panel
- Drug risk assessment table
- Detailed drug-by-drug reports
- Variant detection table

✅ **Data Management**

- JSON export functionality
- Copy-to-clipboard support
- Browser-based analysis history
- Session persistence with localStorage

---

## 📋 Prerequisites

### System Requirements

- **OS:** Windows, macOS, or Linux
- **Memory:** Minimum 2GB RAM
- **Storage:** At least 500MB free space

### Required Software

**Backend:**

- Python 3.8 or higher
- pip (Python package manager)

**Frontend:**

- Node.js 16.0 or higher
- npm 7.0 or higher

### API Keys

- **Google Gemini API Key** (for AI explanations)
  - Sign up at: https://ai.google.dev/
  - Get API key from: https://makersuite.google.com/app/apikey

---

## 🛠️ Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Nisarg2615/RIFT2026.git
cd RIFT2026
```

### Step 2: Backend Setup

#### 2.1 Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 2.2 Install Python Dependencies

```bash
pip install -r requirements.txt
```

**Expected packages:**

- fastapi>=0.110.0
- uvicorn[standard]>=0.29.0
- python-dotenv>=1.0.0
- pydantic>=2.6.0
- google-generativeai>=0.5.0
- pytest>=8.0 (testing)
- httpx>=0.27 (testing)

#### Verify Installation

```bash
python -c "import fastapi; print(f'FastAPI {fastapi.__version__} installed')"
```

### Step 3: Frontend Setup

#### 3.1 Install Node.js Dependencies

```bash
cd frontend
npm install
```

**Expected packages:**

- react@^18.2.0
- vite@^5.0.8
- tailwindcss@^3.3.6
- framer-motion@^10.16.16
- lucide-react@^0.294.0

#### 3.2 Build Frontend (Production)

```bash
npm run build
```

This creates an optimized build in `frontend/build/` directory.

---

## ⚙️ Configuration

### 1. Create Environment File

Create a `.env` file in the project root:

```bash
touch .env  # macOS/Linux
# or
type nul > .env  # Windows
```

### 2. Configure Environment Variables

Add the following to your `.env` file:

```env
# API Configuration
GEMINI_API_KEY=your-google-gemini-api-key-here

# CORS Configuration
CORS_ORIGINS=["http://localhost:3000", "http://localhost:8000"]

# Application Settings
APP_NAME=PharmaGuard
APP_VERSION=1.0.0

# Supported Drugs (comma-separated)
SUPPORTED_DRUGS=Warfarin,Clopidogrel,Metoprolol,Simvastatin,Sertraline,Codeine

# Supported Genes (comma-separated)
SUPPORTED_GENES=CYP2C9,CYP2C19,CYP2D6,CYP3A4,TPMT,SLCO1B1,ADRA2A,HLA-B
```

### 3. Get Your Google Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy the generated key
4. Paste it in your `.env` file as `GEMINI_API_KEY`

### 4. Verify Configuration

```bash
python -c "from src.core.config import get_settings; s = get_settings(); print(f'App: {s.app_name}, Gemini: {bool(s.gemini_api_key)}')"
```

---

## 🚀 Running the Application

### Option 1: Development Mode (Recommended for First-Time Setup)

#### Terminal 1: Backend Server

```bash
# From project root
cd ..  # if in frontend directory
python -m uvicorn src.main:app --reload --port 8000
```

Expected output:

```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

#### Terminal 2: Frontend Development Server

```bash
cd frontend
npm run dev
```

Expected output:

```
  VITE v5.0.8  ready in XXX ms

  ➜  Local:   http://localhost:5173/
```

**Access the application:** http://localhost:8000

### Option 2: Production Mode

#### 2.1 Build Frontend

```bash
cd frontend
npm run build
```

#### 2.2 Run Backend with Built Frontend

```bash
cd ..
python -m uvicorn src.main:app --port 8000
```

**Access the application:** http://localhost:8000

### Option 3: Docker (Optional)

```bash
# Build Docker image
docker build -t pharmaguard:latest .

# Run container
docker run -p 8000:8000 \
  -e GEMINI_API_KEY=your-api-key \
  pharmaguard:latest
```

---

## 📚 API Documentation

### Base URL

```
http://localhost:8000/api
```

### Interactive API Docs

Once the backend is running, visit:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

---

### Endpoints

#### 1. Health Check

**Endpoint:** `GET /api/health`

**Description:** Check API status and configuration

**Response (200 OK):**

```json
{
  "status": "ok",
  "gemini_configured": true,
  "supported_drugs": [
    "Warfarin",
    "Clopidogrel",
    "Metoprolol",
    "Simvastatin",
    "Sertraline",
    "Codeine"
  ],
  "supported_genes": [
    "CYP2C9",
    "CYP2C19",
    "CYP2D6",
    "CYP3A4",
    "TPMT",
    "SLCO1B1",
    "ADRA2A",
    "HLA-B"
  ]
}
```

**Example cURL:**

```bash
curl -X GET "http://localhost:8000/api/health"
```

---

#### 2. Pharmacogenomic Analysis (Main Endpoint)

**Endpoint:** `POST /api/analyze`

**Description:** Analyze VCF file and predict drug safety risks

**Request Headers:**

```
Content-Type: multipart/form-data
```

**Request Parameters:**

| Parameter         | Type        | Required | Description                               |
| ----------------- | ----------- | -------- | ----------------------------------------- |
| `vcf_file`        | File (.vcf) | Yes      | VCF genetic variant file                  |
| `drugs`           | string      | Yes      | Comma-separated drug names (1-6)          |
| `patient_id`      | string      | No       | Optional patient identifier               |
| `patient_history` | JSON        | No       | Optional patient demographics and history |

**Patient History JSON Schema:**

```json
{
  "age": 45,
  "gender": "Male",
  "weight_kg": 75.5,
  "ethnicity": "Caucasian",
  "blood_group": "O+",
  "conditions": ["Hypertension", "Type 2 Diabetes"],
  "current_medications": ["Lisinopril", "Metformin"],
  "allergies": ["Penicillin"],
  "prior_adverse_reactions": ["Rash from Sulfonamides"],
  "kidney_function": "Normal",
  "liver_function": "Normal",
  "smoking_status": "Never",
  "alcohol_use": "Occasional"
}
```

**Response (200 OK):**

```json
[
  {
    "drug_name": "Warfarin",
    "risk_assessment": {
      "label": "HIGH",
      "percentage": 72,
      "severity": "Severe",
      "reasoning": "Ultra-rapid metabolizer (UM) status may result in reduced drug efficacy, requiring higher doses to achieve therapeutic effect"
    },
    "metabolizer_status": "UM",
    "primary_gene": "CYP2C9",
    "detected_variants": [
      {
        "rsid": "rs1057910",
        "chromosome": "10",
        "position": 96702047,
        "genotype": "G/G",
        "zygosity": "homozygous",
        "star_alleles": "*1/*1"
      }
    ],
    "drug_interactions": [
      {
        "interacting_drug": "Aspirin",
        "severity": "moderate",
        "mechanism": "Both increase bleeding risk; combined use requires careful monitoring"
      },
      {
        "interacting_drug": "NSAIDs",
        "severity": "moderate",
        "mechanism": "NSAIDs may increase anticoagulant effects"
      }
    ],
    "evidence_score": {
      "score": 85,
      "factors": [
        "Well-characterized variant",
        "Strong annotation in ClinVar",
        "Supported by clinical evidence",
        "Population frequency data available"
      ]
    },
    "clinical_recommendations": {
      "dosing": "Monitor INR closely; may require doses 20-30% higher than standard; check every 2 weeks initially",
      "monitoring": "INR monitoring every 2-4 weeks; watch for bleeding signs",
      "contraindication": false,
      "alternative_drugs": ["Apixaban", "Rivaroxaban", "Dabigatran"]
    },
    "llm_explanation": "This patient carries genetic variants that make them an ultra-rapid metabolizer of Warfarin. This means their body breaks down the drug very quickly, which could reduce its effectiveness. As a result, standard doses may not provide adequate anticoagulation for stroke prevention...",
    "quality_metrics": {
      "overall_confidence": 0.86,
      "variant_coverage": 0.95
    }
  }
]
```

**Error Response (400 Bad Request):**

```json
{
  "detail": "No drugs specified. Please select at least 1 drug (maximum 6)."
}
```

**Error Response (422 Unprocessable Entity):**

```json
{
  "detail": [
    {
      "loc": ["body", "vcf_file"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

**Example cURL:**

```bash
curl -X POST "http://localhost:8000/api/analyze" \
  -F "vcf_file=@patient.vcf" \
  -F "drugs=Warfarin,Clopidogrel" \
  -F "patient_id=P12345" \
  -F 'patient_history={"age":45,"gender":"Male"}'
```

**Example Python (requests):**

```python
import requests
import json

url = "http://localhost:8000/api/analyze"
files = {"vcf_file": open("sample.vcf", "rb")}
data = {
    "drugs": "Warfarin,Clopidogrel,Metoprolol",
    "patient_id": "PATIENT-001",
    "patient_history": json.dumps({
        "age": 55,
        "gender": "Female",
        "kidney_function": "Normal"
    })
}

response = requests.post(url, files=files, data=data)
print(response.json())
```

**Example JavaScript (Fetch):**

```javascript
const formData = new FormData();
formData.append("vcf_file", vcfFileInput.files[0]);
formData.append("drugs", "Warfarin,Clopidogrel");
formData.append("patient_id", "PATIENT-001");
formData.append(
  "patient_history",
  JSON.stringify({
    age: 55,
    gender: "Female",
  }),
);

const response = await fetch("http://localhost:8000/api/analyze", {
  method: "POST",
  body: formData,
});

const results = await response.json();
console.log(results);
```

---

### Response Data Model

#### RiskAssessment

```json
{
  "label": "LOW|MODERATE|HIGH|CRITICAL",
  "percentage": 0-100,
  "severity": "Mild|Moderate|Severe|Life-threatening",
  "reasoning": "string explanation"
}
```

#### DetectedVariant

```json
{
  "rsid": "rs1057910",
  "chromosome": "10",
  "position": 96702047,
  "genotype": "G/G",
  "zygosity": "homozygous|heterozygous|hemizygous",
  "star_alleles": "*1/*1"
}
```

#### DrugInteraction

```json
{
  "interacting_drug": "Aspirin",
  "severity": "mild|moderate|severe",
  "mechanism": "interaction explanation"
}
```

#### ClinicalRecommendation

```json
{
  "dosing": "dosing guidance",
  "monitoring": "monitoring requirements",
  "contraindication": false,
  "alternative_drugs": ["Drug1", "Drug2"]
}
```

---

### HTTP Status Codes

| Status | Description                             |
| ------ | --------------------------------------- |
| 200    | Successful analysis                     |
| 400    | Bad request (missing parameters)        |
| 422    | Unprocessable entity (validation error) |
| 500    | Internal server error                   |

---

## 🏗️ Architecture

### System Architecture Diagram

```
┌─────────────────────────────────────────────────┐
│         React Frontend (Vite + Tailwind)        │
│  - Component-based UI                           │
│  - Responsive design                            │
│  - Real-time result visualization               │
│  - LocalStorage for history                     │
└─────────────────────┬───────────────────────────┘
                      │ HTTP/REST
┌─────────────────────┴───────────────────────────┐
│        FastAPI Backend (Python + Pydantic)      │
│  - Request routing & validation                 │
│  - API endpoints                                │
│  - Static file serving                          │
│  - CORS middleware                              │
└─────────────────────┬───────────────────────────┘
                      │
    ┌─────────────────┼─────────────────┐
    │                 │                  │
┌───▼────┐    ┌──────▼──────┐    ┌──────▼────┐
│   VCF  │    │   Analysis  │    │  Google   │
│ Parser │    │   Engine    │    │  Gemini   │
│        │    │  (8-step)   │    │   API     │
└────────┘    └─────────────┘    └───────────┘
```

### Data Flow Pipeline

```
1. VCF Upload →
2. VCF Parsing →
3. Gene Identification →
4. Variant Detection →
5. Phenotype Mapping →
6. Risk Assessment →
7. Clinical Modifier Application →
8. Interaction Detection →
9. Evidence Scoring →
10. LLM Explanation Generation →
11. Results Packaging (JSON) →
12. Results Response
```

---

## 🛠️ Technology Stack

### Frontend

| Technology    | Version | Purpose                 |
| ------------- | ------- | ----------------------- |
| React         | 18.2+   | UI framework            |
| Vite          | 5.0+    | Build tool & dev server |
| Tailwind CSS  | 3.3+    | Styling                 |
| Framer Motion | 10.16+  | Animations              |
| Lucide React  | 0.294+  | Icons                   |

### Backend

| Technology    | Version | Purpose                |
| ------------- | ------- | ---------------------- |
| FastAPI       | 0.110+  | Web framework          |
| Python        | 3.8+    | Language               |
| Uvicorn       | 0.29+   | ASGI server            |
| Pydantic      | 2.6+    | Data validation        |
| Python-dotenv | 1.0+    | Environment management |

### External Services

| Service           | Purpose                 |
| ----------------- | ----------------------- |
| Google Gemini API | AI-powered explanations |

---

## 📁 Project Structure

```
RIFT2026/
├── frontend/                      # React frontend application
│   ├── src/
│   │   ├── components/           # React components
│   │   ├── App.js               # Main app component
│   │   └── index.css            # Global styles
│   ├── public/
│   │   └── index.html           # HTML entry point
│   ├── package.json             # Node dependencies
│   ├── vite.config.js           # Vite configuration
│   └── tailwind.config.js       # Tailwind configuration
│
├── src/                          # Python backend application
│   ├── api/
│   │   └── routes/
│   │       └── analyze.py       # Main analyze endpoint
│   ├── services/                 # Business logic
│   │   ├── vcf_parser.py       # VCF file parsing
│   │   ├── rules_engine.py      # Risk calculation
│   │   ├── evidence_scorer.py   # Evidence scoring
│   │   ├── interaction_checker.py # Drug interactions
│   │   ├── llm_client.py        # Gemini API client
│   │   └── clinical_modifiers.py # Clinical logic
│   ├── models/                   # Data models
│   │   └── schemas.py           # Pydantic schemas
│   ├── core/                     # Core configuration
│   │   └── config.py            # Settings management
│   ├── utils/                    # Utility functions
│   └── main.py                   # FastAPI app initialization
│
├── tests/                        # Test suite
│   └── test_analysis.py         # Integration tests
│
├── sample_data/                  # Example data
│   └── *.vcf                    # Sample VCF files
│
├── .env                         # Environment variables (create this)
├── .gitignore                   # Git ignore rules
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── SRS_Report.md               # Detailed specification
├── USER_FLOW_DIAGRAM.md        # User flow diagrams
└── LINKEDIN_PROJECT_SUMMARY.md # Project overview
```

---

## 👨‍💻 Development Guide

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_analysis.py
```

### Code Style

```bash
# Format code with black (if installed)
black src/ frontend/src

# Lint with pylint (if installed)
pylint src/
```

### Adding New Features

1. **Backend:** Add endpoint in `src/api/routes/`
2. **Frontend:** Create component in `frontend/src/components/`
3. **Tests:** Add tests in `tests/`
4. **Documentation:** Update relevant docs

### Common Development Tasks

```bash
# Install new Python package
pip install package-name
pip freeze > requirements.txt

# Install new frontend package
cd frontend
npm install package-name
npm install --save-dev package-name  # for dev-only

# Update all dependencies
cd frontend && npm update && cd ..
pip install --upgrade -r requirements.txt
```

---

## � Deployment

### Deployment Architecture Overview

PharmaGuard is a full-stack application with:

- **Frontend:** React/Vite (Static Site) → Deploy to Netlify ✅
- **Backend:** FastAPI/Python (Server) → Deploy to alternatives (Railway, Render, Heroku, etc.)

**⚠️ Important:** Netlify **cannot** directly host Python FastAPI servers. It only supports:

- Static sites (HTML, CSS, JS)
- Serverless functions (limited)
- Node.js backends

---

### Frontend Deployment (Netlify)

#### Step 1: Deploy Frontend Only (Without Backend)

If you want to deploy just the frontend to showcase the UI:

**1.1 Build the Frontend**

```bash
cd frontend
npm install
npm run build
```

This creates an optimized build in `frontend/build/` directory.

**1.2 Deploy to Netlify via CLI**

```bash
# Install Netlify CLI globally
npm install -g netlify-cli

# Login to Netlify
netlify login

# Deploy from the build directory
cd build
netlify deploy --prod
```

**1.3 Deploy to Netlify via GitHub (Recommended)**

1. Push your code to GitHub:

```bash
git add .
git commit -m "Deploy: prepare for Netlify"
git push origin main
```

2. Go to [Netlify](https://app.netlify.com/)
3. Click **"New site from Git"**
4. Select **GitHub** and authorize
5. Choose your **RIFT2026 repository**
6. Configure build settings:
   - **Base directory:** `frontend`
   - **Build command:** `npm install && npm run build`
   - **Publish directory:** `frontend/build`
7. Set **Environment Variables:**
   - Click **"Show advanced"** → **"New variable"**
   - Add: `REACT_APP_API_URL=https://your-backend-url.com/api`
8. Click **"Deploy site"**

**1.4 Environment Configuration for Frontend**

Create `frontend/.env.production`:

```env
VITE_API_URL=https://your-backend-url.com/api
```

Update `frontend/src/main.jsx` or relevant API call file:

```javascript
const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000/api";
```

---

### Backend Deployment Options

Since FastAPI requires a Python server, here are the best alternatives:

#### Option A: Railway (⭐ Recommended - Easiest)

**Advantages:**

- Easy GitHub integration
- Auto-deploys on push
- Free tier available ($5/month after)
- Python support

**Steps:**

1. **Create Railway Account:**
   - Go to [railway.app](https://railway.app/)
   - Sign up with GitHub

2. **Deploy Backend:**

   ```bash
   git push origin main
   ```

3. **Create `railway.toml` in project root:**

```toml
[build]
builder = "dockerfile"

[deploy]
startCommand = "python -m uvicorn src.main:app --host 0.0.0.0 --port $PORT"
```

4. Create `Procfile` in project root:

```
web: python -m uvicorn src.main:app --host 0.0.0.0 --port $PORT
```

5. In Railway Dashboard:
   - Connect your GitHub repo
   - Set Environment Variables:
     - `GEMINI_API_KEY=your-key`
     - `CORS_ORIGINS=["https://your-netlify-url.netlify.app"]`
   - Railway generates a URL (e.g., `https://project-production.up.railway.app`)

6. Update frontend with backend URL:
   - Go to Netlify → Site Settings → Build & Deploy
   - Set `REACT_APP_API_URL=https://your-railway-url`
   - Redeploy

---

#### Option B: Render.com

**Advantages:**

- Free tier available
- Easy GitHub integration
- Auto-deploys

**Steps:**

1. Go to [render.com](https://render.com/)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure:
   - **Name:** `pharmaguard-api`
   - **Environment:** `Python 3.11`
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `python -m uvicorn src.main:app --host 0.0.0.0`
5. Set Environment Variables:
   - `GEMINI_API_KEY=your-key`
   - `CORS_ORIGINS=["https://your-site.netlify.app"]`
6. Deploy and get your URL

---

#### Option C: Heroku (Paid - No Longer Free)

**If you have existing credits:**

```bash
# Install Heroku CLI
npm install -g heroku

# Login
heroku login

# Create app
heroku create pharmaguard-api

# Set environment variables
heroku config:set GEMINI_API_KEY=your-key

# Deploy
git push heroku main
```

---

#### Option D: AWS Lambda + API Gateway

**Technical but most scalable:**

1. Use Zappa to deploy FastAPI to Lambda:

```bash
pip install zappa
zappa init
zappa deploy production
```

2. Get your API Gateway URL

---

### Full-Stack Deployment (Complete Setup)

#### Step 1: Deploy Frontend to Netlify

Follow the "Deploy to Netlify via GitHub" section above.

Get your Netlify URL: `https://your-site.netlify.app`

#### Step 2: Deploy Backend to Railway/Render

Choose Railway or Render and follow steps above.

Get your Backend URL: `https://your-api-url.railway.app` or `https://your-api-url.onrender.com`

#### Step 3: Connect Frontend & Backend

**3.1 Update Frontend Environment:**

In Netlify Dashboard:

1. Go to **Site Settings** → **Build & Deploy** → **Environment**
2. Add variable: `VITE_API_URL=https://your-api-url.railway.app/api`
3. Trigger redeploy

**3.2 Update Backend CORS:**

In your backend deployment (Railway/Render):

1. Set environment variable: `CORS_ORIGINS=["https://your-site.netlify.app"]`
2. Redeploy

**3.3 Test Connection:**

```bash
curl https://your-api-url.railway.app/api/health
```

Should return:

```json
{
  "status": "ok",
  "gemini_configured": true,
  ...
}
```

#### Step 4: Verify Full Application

1. Open `https://your-site.netlify.app`
2. Upload a VCF file
3. Submit analysis
4. Verify results display properly

---

### Production Checklist

- [ ] Frontend built and deployed to Netlify
- [ ] Backend deployed to Railway/Render/Heroku
- [ ] Environment variables set in both services
- [ ] CORS properly configured
- [ ] API health check passes
- [ ] File upload works
- [ ] Analysis completes successfully
- [ ] Results display correctly
- [ ] Export functionality works
- [ ] Custom domain configured (optional)
- [ ] SSL/HTTPS enabled (automatic on Netlify & Railway)
- [ ] Monitoring/logging enabled

---

### Post-Deployment Configuration

#### Custom Domain (Netlify)

1. Go to **Site Settings** → **Domain Management**
2. Click **Add custom domain**
3. Enter your domain
4. Follow DNS instructions
5. Wait 24-48 hours for DNS propagation

#### Performance Monitoring

Set up monitoring on both services:

- Netlify: Analytics tab
- Railway: Deployments dashboard
- Use Google Analytics for frontend

#### Logging

**Frontend:** Use browser console + Netlify logs

```
Netlify Dashboard → Analytics
```

**Backend:** Check deployment logs

```
Railway: Logs tab
Render: Logs section
```

---

### Cost Breakdown (Monthly)

| Service           | Free Tier            | Paid Starting At         |
| ----------------- | -------------------- | ------------------------ |
| Netlify Frontend  | ✅ (100GB bandwidth) | $19/month                |
| Railway Backend   | ✅ ($5 credit/month) | $5/month (pay-as-you-go) |
| Render Backend    | ✅ (limited)         | $7/month                 |
| Google Gemini API | Free tier available  | Varies by usage          |
| **Total**         | **~$0-5/month**      | **~$24+/month**          |

---

### Troubleshooting Deployments

**Issue: "Failed to deploy frontend"**

```bash
# Ensure build directory is created
cd frontend && npm run build
# Check build output exists
ls build/
```

**Issue: "Backend returns 503 Service Unavailable"**

- Check deployment service status
- Verify environment variables are set
- Check application logs

**Issue: "CORS errors in browser"**

- Update `CORS_ORIGINS` in backend
- Ensure frontend URL matches exactly
- Redeploy backend after CORS update

**Issue: "Netlify function timeout"**

- Increase backend timeout settings
- Consider upgrading Render/Railway plan
- Optimize VCF parsing logic

---

## �🐛 Troubleshooting

### Backend Issues

**Issue: "ModuleNotFoundError: No module named 'fastapi'"**

```bash
# Solution: Install dependencies
pip install -r requirements.txt
```

**Issue: "GEMINI_API_KEY not configured"**

```bash
# Solution: Add to .env file
GEMINI_API_KEY=your-api-key-here
```

**Issue: Port 8000 already in use**

```bash
# Solution: Use different port
python -m uvicorn src.main:app --port 8001
```

### Frontend Issues

**Issue: "npm: command not found"**

```bash
# Solution: Install Node.js from https://nodejs.org/
node --version  # verify installation
```

**Issue: "Module not found" errors**

```bash
# Solution: Reinstall node_modules
rm -rf node_modules package-lock.json
npm install
```

**Issue: Port 5173 already in use**

```bash
# Solution: Use different port
npm run dev -- --port 3000
```

### Common Issues

| Issue                   | Solution                                                    |
| ----------------------- | ----------------------------------------------------------- |
| API 404 error           | Check API endpoint URL and backend running                  |
| File upload fails       | Ensure VCF file format is valid                             |
| No results displayed    | Check browser console for errors; verify .env config        |
| LLM explanation missing | Check GEMINI_API_KEY configuration; API may be rate-limited |

---

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### Steps to Contribute

1. **Fork the Repository**

   ```bash
   git clone https://github.com/YOUR-USERNAME/RIFT2026.git
   ```

2. **Create New Branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**
   - Follow code style guidelines
   - Add tests for new features
   - Update documentation

4. **Commit Changes**

   ```bash
   git commit -m "Add: description of changes"
   ```

5. **Push to Branch**

   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create Pull Request**
   - Describe changes clearly
   - Link related issues
   - Request reviewers

### Code Guidelines

- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small
- Write tests for new functionality
- Update README for new features

---

## 📚 Documentation

Comprehensive documentation is available:

- **[SRS Report](./SRS_Report.md)** - Complete system specification (14 sections)
- **[User Flow Diagrams](./USER_FLOW_DIAGRAM.md)** - Visual user workflows (10 diagrams)
- **[LinkedIn Summary](./LINKEDIN_PROJECT_SUMMARY.md)** - Project overview
- **[Documentation Index](./DOCUMENTATION_INDEX.md)** - All documentation guide
- **[API Docs (Interactive)](http://localhost:8000/docs)** - Swagger UI when running

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 RIFT2026 Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

---

## 📞 Support & Contact

- **GitHub Issues:** Report bugs and request features
- **Documentation:** See SRS_Report.md for detailed specifications
- **Questions:** Check Troubleshooting section

---

## 🌟 Acknowledgments

- Built with ❤️ using modern full-stack technologies
- Pharmacogenomics data sourced from clinical guidelines
- AI explanations powered by Google Gemini API

---

**Version:** 1.0.0  
**Last Updated:** February 2026  
**Status:** Active Development  
**Repository:** https://github.com/Nisarg2615/RIFT2026
