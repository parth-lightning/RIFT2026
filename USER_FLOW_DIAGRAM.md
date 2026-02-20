# User Flow Diagram - PharmaGuard

This document contains the user flow diagrams in Mermaid format for the PharmaGuard Pharmacogenomic Risk Prediction System.

## 1. Main User Flow Diagram

```mermaid
graph TD
    A[="👤 User Visits PharmaGuard"=] --> B{Load Type?}
    B -->|First Visit| C["🏠 View Landing Page<br/>- Title & Description<br/>- Quick Start Guide<br/>- Sample Data Option"]
    B -->|Returning User| D{History Available?}
    D -->|Show History| E["📋 Display Previous<br/>Analyses"]
    D -->|No History| C
    E -->|View Previous Result| F["📊 Display Analysis<br/>Results"]
    E -->|New Analysis| C

    C -->|Click Demo| G["📥 Load Sample Data<br/>- VCF File Loaded<br/>- Sample Drugs Selected"]
    C -->|Upload File| H["📁 Upload VCF File<br/>- Drag & Drop<br/>- File Selector"]

    G --> I["💊 Select Drugs<br/>1-6 from List:<br/>- Warfarin<br/>- Clopidogrel<br/>- Metoprolol<br/>- Simvastatin<br/>- Sertraline<br/>- Codeine"]
    H --> I

    I --> J{Include Patient<br/>History?}
    J -->|Yes| K["👨‍⚕️ Enter Patient History<br/>- Demographics<br/>- Medical History<br/>- Organ Function<br/>- Lifestyle Factors"]
    J -->|No| L["✅ Ready to Analyze"]
    K --> L

    L --> M{Selected?}
    M -->|Validate| N{Valid Input?}
    N -->|Invalid| O["❌ Error Notification<br/>- Show Error Message<br/>- Highlight Issues"]
    O --> L
    N -->|Valid| P["🔄 Send to Backend<br/>POST /api/analyze<br/>- VCF File<br/>- Drug List<br/>- Patient History"]

    P --> Q["⏳ Show Loading State<br/>- Spinner Animation<br/>- Processing Message<br/>- Cancel Status"]

    Q --> R["🧬 Backend Processing<br/>- Parse VCF<br/>- Identify Genes<br/>- Calculate Phenotypes<br/>- Apply Clinical Modifiers<br/>- Check Interactions<br/>- Score Evidence<br/>- Generate LLM Text"]

    R --> S{Processing<br/>Success?}
    S -->|Failed| T["⚠️ Error Handling<br/>- Display Error Message<br/>- Offer Retry<br/>- Clear/Reset Option"]
    T --> C
    S -->|Success| U["📊 Display Results<br/>Complete Analysis"]

    U --> V["🎯 Show Summary Dashboard<br/>- Risk Level (Color)<br/>- Metabolizer Status<br/>- Gene Count<br/>- Drug Count<br/>- Alert Count"]

    V --> W["🧬 Show Gene Panel<br/>Gene Cards with:<br/>- Gene Name<br/>- Star Alleles<br/>- Phenotype Badge<br/>- Function Description"]

    W --> X["💊 Show Drug Risk Table<br/>Columns:<br/>- Drug Name<br/>- Risk Label<br/>- Risk Percentage<br/>- Severity<br/>- Details Button"]

    X --> Y["📝 Show Detailed Reports<br/>For Each Drug:<br/>- Patient Info<br/>- Clinical Modifiers<br/>- Variants Table<br/>- Interactions<br/>- Evidence Score<br/>- Recommendations<br/>- AI Explanation"]

    Y --> Z{User Action?}
    Z -->|Download JSON| AA["💾 Export Analysis<br/>- Generate JSON<br/>- Trigger Download<br/>- Timestamp Included"]
    Z -->|Copy to Clipboard| AB["📋 Copy to Clipboard<br/>- JSON Copied<br/>- Show Confirmation"]
    Z -->|New Analysis| C
    Z -->|View History| E
    Z -->|Scroll| Y

    AA --> AC{Continue?}
    AB --> AC
    AC -->|New Analysis| C
    AC -->|Exit| AD["👋 Session Ends<br/>Results Saved to<br/>Browser History"]
```

## 2. File Upload & Validation Flow

```mermaid
graph TD
    A["📁 User Initiates File Upload"] --> B{Upload Method?}
    B -->|Drag & Drop| C["📥 Drag VCF File<br/>into Drop Zone"]
    B -->|Click to Browse| D["📂 Open File Dialog<br/>Filter: *.vcf files"]

    C --> E["🔍 Validate File"]
    D --> E

    E --> F{File Valid?}
    F -->|Invalid Format| G["❌ Format Error<br/>-Show Error Message<br/>- Suggest Correct Format"]
    F -->|File Too Large| H["❌ Size Error<br/>- Max 50MB<br/>- Suggest Compression"]
    F -->|Invalid Structure| I["❌ Structure Error<br/>- Missing VCF Headers<br/>- Invalid Variants"]
    F -->|Valid| J["✅ File Accepted<br/>- Display File Name<br/>- Show File Size<br/>- Show File Icon"]

    G --> K["🔄 Allow Retry<br/>Cancel or<br/>Select Different File"]
    H --> K
    I --> K
    K --> A

    J --> L["📊 Parse VCF Content<br/>- Extract Headers<br/>- Count Variants<br/>- Identify Genes<br/>- Extract Genotypes"]

    L --> M["✨ Show Preview<br/>- Variant Count<br/>- Gene List<br/>- Sample Data Points"]

    M --> N["➡️ Proceed to<br/>Drug Selection"]
```

## 3. Drug Selection & History Flow

```mermaid
graph TD
    A["💊 Drug Selection Screen"] --> B["📋 Display 6 Available Drugs<br/>1. Warfarin<br/>2. Clopidogrel<br/>3. Metoprolol<br/>4. Simvastatin<br/>5. Sertraline<br/>6. Codeine"]

    B --> C{Selection Method?}
    C -->|Manual Selection| D["☑️ Click Checkboxes<br/>- Enable 1-6 drugs<br/>- Show Selection Count<br/>- Real-time Validation"]
    C -->|Load Sample| E["📌 Load Sample Data<br/>- Pre-select Common Drugs<br/>- Load Sample VCF<br/>- Load Sample History"]

    D --> F{Selection Valid?}
    E --> F
    F -->|No Selection| G["❌ Validation Error<br/>- Require Min 1 Drug<br/>- Max 6 Drugs"]
    G --> D
    F -->|Valid| H["✅ Selection Confirmed<br/>- Show Selected Drugs<br/>- Show Drug Count"]

    H --> I{History Available?}
    I -->|Show History| J["⏱️ Display Analysis History<br/>- Timestamp<br/>- Drugs Analyzed<br/>- Risk Summary<br/>- Load/Delete Options"]
    I -->|No History| K["➡️ Continue to<br/>Patient History Step"]
    J --> L{User Action?}
    L -->|Load Previous| M["📊 Load Analysis<br/>Display Results"]
    L -->|Delete Entry| N["🗑️ Remove from History<br/>Confirmation Required"]
    L -->|New Analysis| K
    N --> J
    M --> O["👋 End Flow"]
    K --> P["Patient History Input"]
```

## 4. Patient History Input Flow

```mermaid
graph TD
    A["👨‍⚕️ Patient History Section<br/>Optional Input"] --> B["Toggle Patient History Form"]

    B --> C{Show Details?}
    C -->|Collapsed| D["🔽 Click to Expand<br/>- Demographics<br/>- Medical History<br/>- Organ Function<br/>- Lifestyle"]
    C -->|Expanded| E["📝 Enter Patient Data"]

    D --> E

    E --> F["👤 Demographics<br/>- Age (numeric)<br/>- Gender (dropdown)<br/>- Weight (kg)<br/>- Ethnicity (text)<br/>- Blood Group (dropdown)"]

    F --> G["🏥 Medical History<br/>- Known Conditions<br/>- Current Medications<br/>- Drug Allergies<br/>- Prior Adverse Reactions<br/>- Each as comma-separated list"]

    G --> H["🫀 Organ Function<br/>- Kidney Function<br/>(Normal/Impaired/Severe)<br/>- Liver Function<br/>(Normal/Impaired/Severe)"]

    H --> I["🚬 Lifestyle Factors<br/>- Smoking Status<br/>- Alcohol Use<br/>- Frequency/Amount"]

    I --> J{"History<br/>Input Valid?"}
    J -->|Invalid| K["❌ Validation Error<br/>- Show Invalid Field<br/>- Provide Correct Format<br/>- Allow Correction"]
    K --> E
    J -->|Valid/Empty| L["✅ Patient Data Accepted<br/>- Optional Fields OK<br/>- Ready for Analysis"]

    L --> M["➡️ Ready to Submit"]
```

## 5. Analysis Processing Flow

```mermaid
graph TD
    A["🚀 User Clicks Analyze<br/>Submit Button"] --> B["📤 Prepare Request<br/>POST /api/analyze"]

    B --> C["📦 Package Data<br/>- VCF File<br/>- Selected Drugs<br/>- Patient History<br/>- Session ID"]

    C --> D["⏳ Show Loading State<br/>- Display Spinner<br/>- 'Analyzing...' Message<br/>- Disable Further Input"]

    D --> E["🔄 Backend Processing<br/>START"]

    E --> F["📖 Parse VCF File<br/>- Extract Variants<br/>- Validate Format<br/>- Build Genetic Profile"]

    F --> G["🧬 Identify Genes"]
    G --> H["Process Each Drug"]

    H --> I["🔍 Gene Mapping<br/>- Find Relevant Gene<br/>- Get Baseline Metabolizer<br/>- Check Star Alleles"]

    I --> J["📊 Risk Assessment<br/>- Analyze Variants<br/>- Determine Phenotype<br/>- Calculate Risk %" ]

    J --> K["🏥 Apply Clinical<br/>Modifiers<br/>- Adjust for Patient<br/>History<br/>- Kidney/Liver Status<br/>- Other Drugs"]

    K --> L["💊 Check Drug<br/>Interactions<br/>- Cross-drug<br/>- Drug-History"]

    L --> M["📈 Score Evidence<br/>- Variant Quality<br/>- Annotation Confidence<br/>- Clinical Significance"]

    M --> N["🤖 Generate LLM<br/>Explanation<br/>- Call Google Gemini<br/>- Natural Language<br/>- Clinical Context"]

    N --> O["📋 Build Clinical<br/>Recommendations<br/>- Dosing Guidance<br/>- Monitoring Needs<br/>- Alternatives"]

    O --> P["✅ Create Result<br/>Package"]

    P --> Q["📤 Return to Frontend<br/>PharmaGuardResult[]"]

    Q --> R{Response<br/>Success?}
    R -->|Failed| S["❌ Error Handling<br/>- Log Error<br/>- Return Error Message<br/>- Suggest Retry"]
    S --> T["Show Error to User"]
    R -->|Success| U["📊 Receive Results<br/>Hide Loading<br/>Display Analysis"]

    U --> V["Display Results UI"]
```

## 6. Results Display & Interaction Flow

```mermaid
graph TD
    A["📊 Analysis Complete<br/>Results Received"] --> B["Hide Loading State<br/>Display Results Container"]

    B --> C["🎯 Summary Dashboard<br/>Quick Metrics Widget"]
    C --> D["Risk Level Card<br/>- Color Coded<br/>- Percentage<br/>- Severity"]

    D --> E["Gene Count Badge<br/>- Number of Genes<br/>- Icon"]

    E --> F["Drug Count Badge<br/>- Number of Drugs<br/>- Icon"]

    F --> G["Alert Count Badge<br/>- Critical Alerts<br/>- Warning Count"]

    G --> H{User Scrolls/<br/>Clicks?}
    H -->|Scroll Down| I["🧬 Gene Panel<br/>Gene Cards Section"]

    I --> J["Card for Each Gene<br/>- Gene Name<br/>- Star Alleles<br/>- Phenotype Badge<br/>- Function Info"]

    J --> K{Continue?}
    K -->|Scroll| L["💊 Drug Risk Table<br/>Summary Table"]

    L --> M["Table Rows:<br/>Drug | Risk | % | Severity"]

    M --> N["Row Click/Expand"]

    N --> O["📖 Detailed Report<br/>for Selected Drug"]

    O --> P["Patient Info Grid<br/>Demographics<br/>Clinical Data"]

    P --> Q["🔬 Detected Variants<br/>Table with:<br/>RSID, Genotype,<br/>Zygosity, Star Alleles"]

    Q --> R["💊 Drug Interactions<br/>List:<br/>- Drug Name<br/>- Severity<br/>- Mechanism"]

    R --> S["📈 Evidence Score<br/>Progress Bar<br/>Confidence Factors"]

    S --> T["💡 Clinical<br/>Recommendations<br/>- Dosing<br/>- Monitoring<br/>- Alternatives"]

    T --> U["🤖 AI Explanation<br/>Natural Language<br/>from Gemini"]

    U --> V{User Action?}
    V -->|Scroll Back| L
    V -->|Different Drug| O
    V -->|Export/Download| W["💾 Export Options"]
    V -->|New Analysis| X["Start Over"]

    W --> Y["Choose Format<br/>Download JSON<br/>Copy to Clipboard"]

    Y --> Z["Generate Export<br/>Timestamp<br/>Complete Profile"]

    Z --> AA["Trigger Download<br/>or Copy Confirm"]

    AA --> AB{"Further<br/>Action?"}
    AB -->|Yes| L
    AB -->|No| AC["👋 End Session<br/>Auto-save to History"]
```

## 7. Error Handling & Recovery Flow

```mermaid
graph TD
    A["⚠️ Error Occurs<br/>During Any Step"] --> B{Error Type?}

    B -->|File Upload Error| C["❌ File Error<br/>- Invalid Format<br/>- Too Large<br/>- Corrupted"]
    B -->|Validation Error| D["❌ Input Error<br/>- Missing Required<br/>- Invalid Values<br/>- Constraint Violation"]
    B -->|Backend Error| E["❌ Processing Error<br/>- VCF Parse Failed<br/>- LLM API Down<br/>- Internal Error"]
    B -->|Network Error| F["❌ Connection Error<br/>- Timeout<br/>- No Response<br/>- CORS Issue"]

    C --> G["Show Error UI<br/>- Toast/Alert<br/>- Error Message<br/>- Recovery Option"]
    D --> G
    E --> G
    F --> G

    G --> H{Recovery<br/>Option?}
    H -->|Retry| I["🔄 Retry Request<br/>- Same Parameters<br/>- Exponential Backoff<br/>- 3 Attempts Max"]
    H -->|Clear/Reset| J["🔄 Reset Form<br/>- Clear Input<br/>- Start New"]
    H -->|Close| K["← Back to<br/>Previous Step"]

    I --> L{Retry<br/>Success?}
    L -->|Yes| M["✅ Recovery<br/>Successful<br/>Continue Flow"]
    L -->|No| N["❌ Persistent Error<br/>- Show Details<br/>- Contact Support Info"]

    J --> O["Clear All Fields<br/>Return to Upload"]
    K --> O
    N --> P["Manual Option:<br/>- Download Support<br/>- Email Admin<br/>- Try Later"]
```

## 8. History Management Flow

```mermaid
graph TD
    A["⏱️ Analysis History<br/>Browser LocalStorage"] --> B{History<br/>Available?}

    B -->|No History| C["↪️ Show Empty State<br/>- 'No analyses yet'<br/>- Guide to Start"]
    B -->|Yes| D["📋 Display History List"]

    D --> E["History Item:<br/>- Date/Time<br/>- Drugs<br/>- Risk Summary<br/>- Action Buttons"]

    E --> F{User Click?}
    F -->|View| G["📊 Load Analysis<br/>- Retrieve Stored Result<br/>- Display Same UI<br/>- No Re-Processing"]

    F -->|Delete| H["🗑️ Delete Confirmation<br/>- Are you sure?<br/>- Yes/Cancel"]

    F -->|New Analysis| I["Start Fresh Analysis"]

    H --> J{Confirm?}
    J -->|Yes| K["🗑️ Remove from<br/>LocalStorage"]
    J -->|No| E

    K --> L["📋 Update History<br/>List"]

    L --> M{More<br/>Items?}
    M -->|Yes| E
    M -->|No| N["↪️ Show Empty State"]

    G --> O["Display Results<br/>with Export Options"]

    O --> P["Can Download<br/>Previous Result<br/>as JSON"]
```

## 9. Export & Download Flow

```mermaid
graph TD
    A["💾 User Initiates Export"] --> B{Export Type?}

    B -->|Download JSON| C["📥 Generate JSON<br/>- Full Analysis<br/>- Metadata<br/>- Timestamp"]

    B -->|Copy to Clipboard| D["📋 Copy Full Result<br/>as JSON String"]

    C --> E["Create Blob<br/>with JSON"]

    E --> F["Generate URL<br/>blob:"]

    F --> G["Create Hidden<br/>Link Element"]

    G --> H["Trigger Download<br/>File Name:<br/>pharmaguard_<br/>patientid_<br/>timestamp.json"]

    H --> I["📥 File Downloaded<br/>to User Device"]

    D --> J["Copy String<br/>to Clipboard<br/>API"]

    J --> K["✅ Show Confirmation<br/>'Copied to<br/>Clipboard!'"]

    I --> L{Next Action?}
    K --> L

    L -->|New Analysis| M["Start New"]
    L -->|View Results| N["Show Results"]
    L -->|Close| O["👋 End Session"]

    M --> P["Reset to Upload"]
    N --> Q["Display Results UI"]
```

## 10. Session Flow - Complete Journey

```mermaid
graph LR
    A["🔵 START<br/>User Opens App"]

    A -->|First Time| B["🌐 Landing Page"]
    A -->|Returning| C{History?}

    C -->|Yes| D["📋 Show History"]
    C -->|No| B

    B --> E["📁 Upload/Demo<br/>VCF File"]
    D --> F{Choice?}
    F -->|Load Old| G["Display Result"]
    F -->|New Analysis| E

    E --> H["💊 Select Drugs"]
    H --> I["👨‍⚕️ Enter History<br/>Optional"]
    I --> J["🚀 Submit Analysis"]
    J --> K["⏳ Processing"]
    K --> L["📊 Results Display"]

    L --> M{User Action?}
    M -->|Export| N["💾 Download JSON"]
    M -->|New| E
    M -->|History| D
    M -->|Exit| O{Session Over?}

    N --> P{Continue?}
    P -->|Yes| M
    P -->|No| O

    G --> Q{Continue?}
    Q -->|Yes| M
    Q -->|No| O

    O -->|Save| R["💾 Auto-save<br/>to History"]
    O -->|Discard| S["🗑️ Skip"]

    R --> T["🔴 END<br/>Session Closed"]
    S --> T
```

---

## Diagram Legend

| Symbol | Meaning            |
| ------ | ------------------ |
| 🔵     | Start Node         |
| 🔴     | End Node           |
| ➡️     | Process Flow       |
| ❌     | Error State        |
| ✅     | Success State      |
| ⏳     | Loading/Processing |
| 💾     | Storage/Save       |
| 📊     | Display/Report     |
| 💊     | Drug Related       |
| 🧬     | Genetic Data       |
| 👨‍⚕️     | Patient/Clinical   |
| 🤖     | AI/LLM             |
| 🔄     | Retry/Repeat       |

---

## User Journey Summary

1. **Landing** → User visits app
2. **Upload** → Select VCF file (manual or demo)
3. **Selection** → Choose 1-6 drugs
4. **History** → Optional patient info
5. **Analysis** → Backend processes request
6. **Results** → View comprehensive reports
7. **Export** → Download JSON or copy
8. **History** → Auto-saved for future reference

---

_This user flow diagram provides a complete visualization of user interactions with the PharmaGuard system, from initial landing through result export and session management._
