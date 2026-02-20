# Software Requirements Specification (SRS)

## PharmaGuard - Pharmacogenomic Risk Prediction System

**Project Name:** RIFT2026 - PharmaGuard  
**Version:** 1.0.0  
**Date:** February 2026  
**Author:** Development Team  
**Status:** Active Development

---

## 1. Executive Summary

PharmaGuard is a web-based pharmacogenomic analysis platform that predicts drug safety risks based on patient genetic profiles. The system integrates genomic data (VCF files), drug information, and clinical history to provide comprehensive risk assessments, drug interaction predictions, and AI-generated clinical recommendations.

**Key Value Proposition:**

- Reduce adverse drug reactions through personalized pharmacogenomic analysis
- Provide evidence-based clinical recommendations for healthcare providers
- Enable data-driven medication selection based on genetic profiles
- Support precision medicine initiatives in clinical practice

---

## 2. Scope

### 2.1 In Scope

- VCF (Variant Call Format) file upload and parsing
- Analysis of genetic variants against 6 supported medications
- Drug-drug interaction detection
- Clinical risk stratification
- Evidence-based accuracy scoring
- AI-generated clinical explanations and recommendations
- Patient history management
- Detailed reporting and export capabilities
- Web-based user interface
- RESTful API backend

### 2.2 Out of Scope

- Patient data storage/persistence (analysis only)
- Electronic Health Record (EHR) integration
- Direct prescribing capabilities
- Clinical trial management
- Diagnostic certification/FDA approval
- Multi-tenant support in v1.0

---

## 3. Functional Requirements

### 3.1 File Upload & Validation (FR-1)

**Requirement:** System shall accept and validate VCF files from users.

**Detailed Requirements:**

- **FR-1.1:** Accept VCF format files (minimum viable structure)
- **FR-1.2:** Validate VCF file format and structure
- **FR-1.3:** Parse VCF headers and variant entries
- **FR-1.4:** Extract genomic coordinates, genotypes, and quality metrics
- **FR-1.5:** Display validation errors with specific error messages
- **FR-1.6:** Support files up to 50MB in size

**Acceptance Criteria:**

- Valid VCF files are processed without errors
- Invalid files are rejected with descriptive error messages
- Processing completes within 30 seconds for standard files

---

### 3.2 Drug Selection & Metadata (FR-2)

**Requirement:** System shall support selection of medications for analysis.

**Detailed Requirements:**

- **FR-2.1:** Display list of 6 supported medications
- **FR-2.2:** Allow multi-select (user can choose 1-6 drugs)
- **FR-2.3:** Store drug metadata (names, therapeutic categories)
- **FR-2.4:** Provide sample data option for demonstration

**Supported Drugs:**

1. Warfarin - Anticoagulant
2. Clopidogrel - Antiplatelet
3. Metoprolol - Beta-blocker
4. Simvastatin - Statins
5. Sertraline - SSRI Antidepressant
6. Codeine - Opioid Analgesic

**Acceptance Criteria:**

- Users can select minimum 1 and maximum 6 drugs
- Drug list is clearly displayed and easily selectable
- Sample data loads within 2 seconds

---

### 3.3 Pharmacogenomic Analysis (FR-3)

**Requirement:** System shall perform comprehensive genetic risk analysis for selected drugs.

**Detailed Requirements:**

- **FR-3.1:** Identify relevant genes for each selected drug
- **FR-3.2:** Detect genetic variants from VCF data
- **FR-3.3:** Map variants to phenotypes (IM, PM, NM, UM)
- **FR-3.4:** Calculate metabolic phenotype for each gene-drug combination
- **FR-3.5:** Apply clinical modifier rules based on patient history
- **FR-3.6:** Return drug-specific results within analysis results

**Phenotype Mappings:**

- **PM (Poor Metabolizer):** Cannot metabolize drug effectively → High toxicity risk
- **IM (Intermediate Metabolizer):** Reduced metabolism → Moderate risk
- **NM (Normal Metabolizer):** Normal metabolism → Standard dosing
- **UM (Ultra-rapid Metabolizer):** Rapid metabolism → Reduced efficacy risk

**Acceptance Criteria:**

- Analysis completes within 60 seconds for standard input
- Phenotypes are correctly determined based on star allele assignments
- Clinical modifiers are appropriately applied

---

### 3.4 Risk Assessment & Stratification (FR-4)

**Requirement:** System shall calculate and categorize drug safety risks.

**Detailed Requirements:**

- **FR-4.1:** Assign risk labels: LOW, MODERATE, HIGH, CRITICAL
- **FR-4.2:** Calculate risk percentage (0-100%)
- **FR-4.3:** Define severity levels: Mild, Moderate, Severe, Life-threatening
- **FR-4.4:** Provide actionable risk reasoning
- **FR-4.5:** Consider metabolizer status, variant impact, and clinical modifiers

**Risk Stratification Matrix:**
| Risk Level | Percentage | Clinical Implication |
|------------|-----------|----------------------|
| LOW | 0-25% | Standard dosing recommended |
| MODERATE | 26-50% | Monitor dosing; consider adjustment |
| HIGH | 51-75% | Dose adjustment recommended |
| CRITICAL | 76-100% | Alternative drug strongly recommended |

**Acceptance Criteria:**

- Risk calculations are consistent and reproducible
- Risk labels align with percentage values
- Clinical implications are medically sound

---

### 3.5 Drug-Drug Interaction Detection (FR-5)

**Requirement:** System shall identify and report potential drug-drug interactions.

**Detailed Requirements:**

- **FR-5.1:** Detect interactions between selected drugs
- **FR-5.2:** Classify interaction severity (mild, moderate, severe)
- **FR-5.3:** Provide interaction mechanism explanation
- **FR-5.4:** Suggest management strategies
- **FR-5.5:** Cross-reference with patient's current medications from history

**Interaction Severity:**

- **Mild:** Minimal clinical impact; monitor
- **Moderate:** Potential clinical consequences; manage
- **Severe:** Significant risk; avoid combination if possible

**Acceptance Criteria:**

- All relevant interactions are identified
- Severity classifications are appropriate
- Management recommendations are clinically valid

---

### 3.6 Evidence-Based Accuracy Scoring (FR-6)

**Requirement:** System shall provide confidence scores for analysis results.

**Detailed Requirements:**

- **FR-6.1:** Calculate evidence score based on variant annotation quality
- **FR-6.2:** Generate score between 0-100%
- **FR-6.3:** Evaluate variant clinical significance
- **FR-6.4:** Consider population frequency and function prediction
- **FR-6.5:** Display score with confidence visualization

**Evidence Calculation Factors:**

- Variant annotation completeness (frequency, function prediction)
- Clinical significance of detected variants
- Population diversity representation
- Phenotype assignment confidence
- Prior clinical evidence availability

**Acceptance Criteria:**

- Scores are consistent for same input
- Scores reflect data quality appropriately
- Visual representation is clear and intuitive

---

### 3.7 Clinical Recommendations (FR-7)

**Requirement:** System shall provide evidence-based clinical guidance.

**Detailed Requirements:**

- **FR-7.1:** Generate drug-specific recommendations
- **FR-7.2:** Consider metabolizer status
- **FR-7.3:** Factor in detected variants
- **FR-7.4:** Include dosing guidance when applicable
- **FR-7.5:** Provide monitoring recommendations
- **FR-7.6:** Suggest alternative drugs when needed

**Recommendation Categories:**

- Dosing adjustments
- Monitoring requirements
- Alternative drug suggestions
- Contraindications
- Drug-food interactions
- Timing and administration notes

**Acceptance Criteria:**

- Recommendations are clinically appropriate
- Guidance is evidence-based and referenced
- Recommendations are actionable for physicians

---

### 3.8 AI-Generated Explanations (FR-8)

**Requirement:** System shall provide natural language explanations of genetic findings.

**Detailed Requirements:**

- **FR-8.1:** Integrate with Google Gemini API for explanation generation
- **FR-8.2:** Generate patient-friendly explanations
- **FR-8.3:** Explain variant significance
- **FR-8.4:** Clarify phenotype implications
- **FR-8.5:** Summarize clinical recommendations
- **FR-8.6:** Maintain medical accuracy while ensuring readability

**Explanation Components:**

- Variant discovery statement
- Gene and metabolic pathway explanation
- Phenotype consequence description
- Drug interaction implications
- Clinical action points

**Acceptance Criteria:**

- Explanations are medically accurate
- Language is clear and understandable
- Generation completes within 30 seconds
- API errors are handled gracefully

---

### 3.9 Patient History Management (FR-9)

**Requirement:** System shall collect and utilize patient clinical history.

**Detailed Requirements:**

- **FR-9.1:** Accept optional patient demographic information
  - Age, gender, weight, ethnicity, blood group
- **FR-9.2:** Capture medical history
  - Conditions, current medications, allergies, adverse reactions
- **FR-9.3:** Include organ function status
  - Kidney function, liver function
- **FR-9.4:** Record lifestyle factors
  - Smoking status, alcohol use
- **FR-9.5:** Apply history-based clinical modifiers to risk assessment
- **FR-9.6:** Flag relevant patient conditions affecting drug metabolism

**Patient History Schema:**

```
{
  "demographics": { age, gender, weight, ethnicity, blood_group },
  "medical_history": { conditions, current_medications, allergies, prior_adverse_reactions },
  "organ_function": { kidney_function, liver_function },
  "lifestyle": { smoking_status, alcohol_use }
}
```

**Acceptance Criteria:**

- History data is optional (not blocking analysis)
- Clinical modifiers are correctly applied
- Patient flags are displayed prominently

---

### 3.10 Detailed Reporting (FR-10)

**Requirement:** System shall generate comprehensive analysis reports.

**Report Sections:**

- **FR-10.1:** Summary Dashboard
  - Overall risk level, primary metabolizer status
  - Gene count, drug count, alert count
  - Quick overview widgets
- **FR-10.2:** Gene Analysis Panel
  - Detected genes with star allele assignments
  - Phenotypes and metabolic status
  - Clinical phenotype data
- **FR-10.3:** Drug Risk Assessment Table
  - Drug names with risk categories
  - Sortable and filterable
  - Quick navigation to detailed reports
- **FR-10.4:** Detailed Drug-by-Drug Reports including:
  - Patient information grid
  - Clinical Risk Modifiers visualization
  - Detected Variants table (RSID, genotype, zygosity, star alleles)
  - Drug-Drug Interactions
  - Evidence-Based Accuracy Scores with progress bars
  - Clinical Recommendations
  - AI-Generated Explanations

**Acceptance Criteria:**

- All sections are present and populate correctly
- Information is organized logically
- Navigation between sections is intuitive

---

### 3.11 Data Export & Download (FR-11)

**Requirement:** System shall allow users to export analysis results.

**Detailed Requirements:**

- **FR-11.1:** Export full analysis as JSON format
- **FR-11.2:** Provide copy-to-clipboard functionality
- **FR-11.3:** Include timestamp and patient identifier
- **FR-11.4:** Preserve all analysis details in export
- **FR-11.5:** Enable data sharing for medical records

**Export Content:**

- Complete pharmacogenomic profile
- All detected variants
- Risk assessments and scores
- Clinical recommendations
- Drug interactions
- Patient metadata

**Acceptance Criteria:**

- JSON export is valid and complete
- Copy functionality works across browsers
- Exported data can be re-imported or shared

---

### 3.12 Analysis History Management (FR-12)

**Requirement:** System shall maintain analysis history for user reference.

**Detailed Requirements:**

- **FR-12.1:** Store analysis results in browser localStorage
- **FR-12.2:** Display previous analysis summaries
- **FR-12.3:** Allow quick retrieval of past analyses
- **FR-12.4:** Clear history option available
- **FR-12.5:** No server-side persistence required

**History Storage:**

- Analysis timestamp
- Patient identifier
- Drug list analyzed
- Summary results
- Full result export

**Acceptance Criteria:**

- History persists within session and browser
- User can navigate to previous analyses
- History UI is clear and accessible

---

## 4. Non-Functional Requirements

### 4.1 Performance (NFR-1)

| Requirement                      | Target                      |
| -------------------------------- | --------------------------- |
| VCF file upload time             | < 5 seconds for <10MB files |
| Analysis processing time         | < 60 seconds per analysis   |
| API response time (health check) | < 200ms                     |
| Frontend load time               | < 2 seconds                 |
| LLM explanation generation       | < 30 seconds                |

**Acceptance Criteria:**

- 95th percentile response times meet targets
- No timeout errors for standard operations
- Graceful degradation for slow networks

---

### 4.2 Scalability (NFR-2)

- **Load Capacity:** Platform should handle 100+ concurrent users
- **Concurrent Analyses:** At least 10 simultaneous analyses
- **File Size:** Support VCF files up to 50MB
- **Data Volume:** Support 1000+ variant records per analysis

---

### 4.3 Reliability & Availability (NFR-3)

- **Uptime Target:** 99% availability during business hours
- **Error Handling:** All error conditions handled gracefully
- **Data Validation:** Comprehensive input validation
- **Error Recovery:** System recovers from API failures

---

### 4.4 Security (NFR-4)

- **Data In Transit:** HTTPS/TLS for all communications
- **API Security:** CORS properly configured
- **Input Validation:** Strict validation of all inputs
- **Error Messages:** No sensitive information in error messages
- **File Upload:** Validate file types and sizes
- **API Keys:** Secure storage of credentials (.env file)

**Security Best Practices:**

- Environment variables for sensitive data
- No hardcoded credentials
- Request/response validation
- Error message sanitization

---

### 4.5 Usability (NFR-5)

- **Interface:** Intuitive, clean, modern design
- **Accessibility:** Basic accessibility standards (color contrast, text size)
- **Mobile Support:** Responsive design for tablets and phones
- **Language:** Clear, non-technical where possible
- **Guidance:** Help text and tooltips for complex features

---

### 4.6 Maintainability (NFR-6)

- **Code Documentation:** Comprehensive docstrings and comments
- **Architecture:** Clean separation of concerns
- **Component Design:** Reusable, modular components
- **Testing:** Unit tests for critical functions
- **Logging:** Structured logging for debugging

---

### 4.7 Compatibility (NFR-7)

- **Browsers:** Chrome, Firefox, Safari (latest 2 versions)
- **Python:** 3.8+
- **Node.js:** 16+
- **OS:** Windows, macOS, Linux

---

## 5. Technical Requirements

### 5.1 Architecture

**System Architecture:** Microservices with Frontend-Backend separation

```
┌─────────────────────────────────────────────────────────┐
│                  React Frontend (Vite)                  │
│  - Component-based UI                                   │
│  - Responsive design (Tailwind CSS)                     │
│  - Real-time state management                           │
│  - Local storage (history, session data)                │
└──────────────────────┬──────────────────────────────────┘
                       │ HTTP/REST
┌──────────────────────┴──────────────────────────────────┐
│              FastAPI Backend (Python)                   │
│  - /api/analyze (main analysis endpoint)               │
│  - /api/health (liveness probe)                        │
│  - /static (frontend assets)                           │
│  - /*(SPA fallback)                                    │
└──────────────────────┬──────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
    ┌───▼──┐    ┌─────▼─────┐    ┌──▼──────┐
    │  VCF │    │   Rules   │    │ Google  │
    │Parser│    │  Engine   │    │ Gemini  │
    └───┬──┘    └─────┬─────┘    └──┬──────┘
        │              │              │
    ┌───┴──────────────┴──────────────┴──┐
    │     Analysis Services Layer       │
    │  - Risk Assessment                │
    │  - Drug Interactions              │
    │  - Evidence Scoring               │
    │  - Clinical Modifiers             │
    │  - LLM Integration                │
    └──────────────────────────────────┘
```

### 5.2 Technology Stack

**Frontend:**

- React 18.2.0 - UI framework
- Vite - Build tool & dev server
- Tailwind CSS - Styling
- Framer Motion - Animations
- Lucide React - Icons

**Backend:**

- FastAPI 0.110.0+ - Web framework
- Uvicorn - ASGI server
- Pydantic - Data validation
- Python 3.8+

**External Services:**

- Google Gemini API - AI explanations
- REST API communication

**Database:**

- None (v1.0 - session-based only)

### 5.3 API Specification

#### POST /api/analyze

**Purpose:** Primary endpoint for pharmacogenomic analysis

**Request:**

```json
{
  "vcf_file": "File - *.vcf file content",
  "drugs": "string - comma-separated drug names",
  "patient_id": "string (optional) - patient identifier",
  "patient_history": "JSON (optional) - patient demographics and history"
}
```

**Response:**

```json
[
  {
    "drug_name": "Warfarin",
    "risk_assessment": {
      "label": "HIGH",
      "percentage": 72,
      "severity": "Severe",
      "reasoning": "Ultra-rapid metabolizer may have reduced efficacy"
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
        "mechanism": "Increased bleeding risk"
      }
    ],
    "evidence_score": {
      "score": 85,
      "factors": ["Well-characterized variant", "Strong annotation"]
    },
    "clinical_recommendations": {
      "dosing": "Monitor INR closely; may need higher doses",
      "monitoring": "Check INR every 2-4 weeks",
      "contraindication": false,
      "alternative_drugs": ["Apixaban", "Rivaroxaban"]
    },
    "llm_explanation": "Detailed natural language explanation...",
    "quality_metrics": {
      "overall_confidence": 0.86,
      "variant_coverage": 0.95
    }
  }
]
```

#### GET /api/health

**Purpose:** Health check and configuration summary

**Response:**

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

---

## 6. Data Model & Schema

### 6.1 Core Schemas

```python
class RiskLabel(Enum):
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class Severity(Enum):
    MILD = "Mild"
    MODERATE = "Moderate"
    SEVERE = "Severe"
    LIFE_THREATENING = "Life-threatening"

class Zygosity(Enum):
    HOMOZYGOUS = "homozygous"
    HETEROZYGOUS = "heterozygous"
    HEMIZYGOUS = "hemizygous"

class RiskAssessment(BaseModel):
    label: RiskLabel
    percentage: float  # 0-100
    severity: Severity
    reasoning: str

class DetectedVariant(BaseModel):
    rsid: str  # e.g., "rs1057910"
    chromosome: str
    position: int
    genotype: str  # e.g., "G/G"
    zygosity: Zygosity
    star_alleles: str  # e.g., "*1/*1"

class DrugInteraction(BaseModel):
    interacting_drug: str
    severity: str  # "mild", "moderate", "severe"
    mechanism: str

class EvidenceScore(BaseModel):
    score: float  # 0-100
    factors: List[str]

class ClinicalRecommendation(BaseModel):
    dosing: str
    monitoring: str
    contraindication: bool
    alternative_drugs: List[str]

class PharmaGuardResult(BaseModel):
    drug_name: str
    risk_assessment: RiskAssessment
    metabolizer_status: str
    primary_gene: str
    detected_variants: List[DetectedVariant]
    drug_interactions: List[DrugInteraction]
    evidence_score: EvidenceScore
    clinical_recommendations: ClinicalRecommendation
    llm_explanation: str
    quality_metrics: QualityMetrics

class PatientHistory(BaseModel):
    # Demographics
    age: Optional[int]
    gender: Optional[str]
    weight_kg: Optional[float]
    ethnicity: Optional[str]
    blood_group: Optional[str]
    # Medical History
    conditions: Optional[List[str]]
    current_medications: Optional[List[str]]
    allergies: Optional[List[str]]
    prior_adverse_reactions: Optional[List[str]]
    # Organ Function
    kidney_function: Optional[str]
    liver_function: Optional[str]
    # Lifestyle
    smoking_status: Optional[str]
    alcohol_use: Optional[str]
```

---

## 7. User Interface Specification

### 7.1 Key Components

1. **Header**
   - App title "PharmaGuard"
   - Navigation menu
   - History button

2. **Upload Section**
   - VCF file upload zone (drag & drop enabled)
   - Drug selection multi-select
   - Patient history form (collapsible)
   - Submit button

3. **Loading State**
   - Spinner animation
   - Progress message
   - Estimated time remaining

4. **Summary Dashboard**
   - Risk level widget (color-coded)
   - Metabolizer status
   - Gene count
   - Drug count
   - Alerts/flags count

5. **Gene Panel**
   - Gene cards with star allele assignments
   - Phenotype badges
   - Gene function description

6. **Drug Risk Table**
   - Searchable/filterable table
   - Drug name, risk level, severity
   - Click to expand details

7. **Detailed Reports**
   - Patient info grid
   - Clinical modifiers visualization
   - Variants table
   - Drug interactions list
   - Evidence score progress bar
   - AI-generated explanation
   - Recommendations section

8. **Download Section**
   - JSON download button
   - Copy to clipboard button
   - Share options

---

## 8. External Dependencies & Integration

### 8.1 Google Gemini API

**Integration Point:** LLM explanation generation for variant significance

**Configuration:**

- API Key stored in environment (.env)
- Endpoint: Google Generative AI API
- Model: gemini-1.5-pro or latest

**Error Handling:**

- Graceful fallback if API unavailable
- Default explanation template if LLM fails
- Retry logic with exponential backoff

### 8.2 Third-party Libraries

**Python:**

- fastapi>=0.110.0
- uvicorn[standard]>=0.29.0
- pydantic>=2.6.0
- python-dotenv>=1.0.0
- google-generativeai>=0.5.0

**JavaScript:**

- react>=18.2.0
- vite>=5.0.8
- tailwindcss>=3.3.6
- framer-motion>=10.16.16
- lucide-react>=0.294.0

---

## 9. Testing Requirements

### 9.1 Test Coverage

**Unit Tests:**

- VCF parsing (valid/invalid inputs)
- Risk calculation logic
- Phenotype determination
- Evidence scoring algorithm
- Clinical modifier application

**Integration Tests:**

- Full API endpoint testing
- VCF to result pipeline
- Patient history influence on results
- LLM integration

**Functional Tests:**

- File upload/validation
- Drug selection
- Analysis execution
- Result download
- History management

**Target Coverage:** >80% code coverage

### 9.2 Test Data

- Sample VCF file with known variants
- Test cases for each supported drug
- Patient history test scenarios
- Negative test cases (invalid inputs)

---

## 10. Deployment & Infrastructure

### 10.1 Deployment Environment

**Frontend:**

- Served from FastAPI StaticFiles
- Built with Vite (npm run build)
- Output to /frontend/build directory

**Backend:**

- FastAPI application (uvicorn)
- Single process (can be scaled with Docker)
- Port: 8000 (configurable)

### 10.2 Environment Configuration

```env
# .env file
GEMINI_API_KEY=<google-api-key>
CORS_ORIGINS=["*"] or specific URLs
APP_NAME=PharmaGuard
APP_VERSION=1.0.0
SUPPORTED_DRUGS=["Warfarin", "Clopidogrel", ...]
```

### 10.3 Deployment Instructions

```bash
# Frontend build
cd frontend
npm install
npm run build

# Backend execution
cd ..
pip install -r requirements.txt
python -m uvicorn src.main:app --reload --port 8000
```

### 10.4 Docker (Optional)

Containerization support can be added for:

- Easy deployment to cloud platforms (Azure, AWS, GCP)
- Microservices architecture scaling
- Isolated environment consistency

---

## 11. Changes & Updates Tracking

### 11.1 v1.0.0 Features

**✅ Implemented:**

- VCF file parsing and validation
- 6 drug support (Warfarin, Clopidogrel, Metoprolol, Simvastatin, Sertraline, Codeine)
- Risk assessment and stratification
- Clinical recommendation generation
- AI-powered natural language explanations
- Drug-drug interaction detection
- Evidence-based accuracy scoring
- Patient history management
- Detailed comprehensive reporting
- Analysis history (localStorage)
- JSON export & download
- React-based modern UI
- FastAPI backend

**🔄 Future Enhancements (v2.0+):**

- Persistent database (PostgreSQL/MongoDB)
- User authentication & authorization
- Additional drug support (50+ medications)
- EHR system integration
- Mobile native app
- Advanced filtering and export formats (CSV, PDF)
- Comparative analysis (before/after treatment)
- Population pharmacogenomics analytics
- FDA-certified variant annotation
- Machine learning model updates

---

## 12. Acceptance Criteria & Sign-Off

### 12.1 System Acceptance

The system shall be considered production-ready when:

✅ All functional requirements (FR-1 through FR-12) are fully implemented  
✅ All non-functional requirements (NFR-1 through NFR-7) are met  
✅ Unit test coverage > 80%  
✅ All critical and major bugs resolved  
✅ Performance benchmarks achieved  
✅ Security review completed  
✅ User acceptance testing passed  
✅ Documentation complete

### 12.2 Known Limitations

1. **No Persistent Storage:** Analysis results stored only in session/localStorage
2. **Limited Drug Support:** Only 6 drugs in initial release
3. **Basic Variant Annotation:** Limited to integrated databases
4. **Single User:** No multi-user support or authentication
5. **Offline Capable:** Some features (LLM explanations) require internet connection

---

## 13. Glossary & Terminology

| Term                            | Definition                                                 |
| ------------------------------- | ---------------------------------------------------------- |
| **Pharmacogenomics**            | Study of how genes affect medication response              |
| **VCF (Variant Call Format)**   | Standard format for storing genetic variant information    |
| **Genotype**                    | Genetic makeup; pair of alleles at a locus                 |
| **Phenotype**                   | Observed characteristics; metabolic capability             |
| **Metabolizer Status**          | Classification of drug metabolism ability (PM, IM, NM, UM) |
| **Star Alleles**                | Specific allelic variants at pharmacogenetic loci          |
| **Adverse Drug Reaction (ADR)** | Harmful, unintended reaction to medication                 |
| **Drug-Drug Interaction**       | Effect of one drug on the action of another                |
| **Evidence Score**              | Confidence metric for analysis accuracy                    |
| **Genotype to Phenotype**       | Conversion of genetic information to metabolic capability  |
| **Clinical Modifier**           | Factor from patient history affecting drug metabolism      |

---

## 14. References & Standards

- **VCF Specification:** SAM/BAM Format Specification (1.0, 2020)
- **Pharmacogenomics Standards:** PharmGKB database guidelines
- **Gene Nomenclature:** HGNC (Hugo Gene Nomenclature Committee)
- **Variant Classification:** ClinVar annotation criteria
- **Clinical Practice Guidelines:** CPIC & FDA PharmGx guidelines

---

**Document Status:** Final  
**Last Updated:** February 2026  
**Next Review:** Q3 2026

---

_This SRS document serves as the comprehensive specification for the PharmaGuard system. All development, testing, and deployment activities should align with requirements defined herein._
