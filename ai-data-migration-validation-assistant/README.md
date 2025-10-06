# 🤖 AI Data Migration Validation Assistant

An AWS-inspired project that automates data migration validation and explains results in natural language using Generative AI concepts.

---

## 🚀 Overview
Data migration from legacy CSVs or on-prem databases to cloud systems (like Amazon RDS or Redshift) often introduces schema mismatches, row count differences, or value inconsistencies.  
This assistant **automates validation** and produces **human-readable summaries**, helping engineers quickly identify and fix migration issues.

---

## ⚙️ What it Does
- Compares source and target datasets:
  - Schema (missing or extra columns)
  - Row counts
  - Value mismatches in shared columns
- Generates a **technical JSON report**
- Produces a **natural-language summary** (mock AI output for demo)

**Example Summary:**
```
✅ Source Rows: 4, Target Rows: 4
⚠️ Missing Columns: ['email', 'dob']
❗ Value Mismatches: 1
✅ Overall Accuracy: 75.0%
Recommendation: Verify ETL mapping for missing fields and mismatched region values.
```

---

## 🏗️ How We Built It
- **Python** – Data validation and logic
- **Pandas** – Handling CSV data comparison
- **AWS Concepts** (for real-world deployment):
  - **Amazon S3** – Store source files
  - **Amazon RDS / Redshift** – Target databases
  - **AWS Lambda** – Serverless validation workflow
  - **Amazon Bedrock** – AI reasoning for summaries
  - **DynamoDB** – Store validation history
  - **CloudWatch** – Logging & monitoring

---

## 📂 Folder Structure
```
ai-data-migration-validation-assistant/
├── README.md
├── validation_agent.py
├── sample_data/
│   ├── customers_source.csv
│   └── customers_target.csv
└── output/
    └── validation_summary.txt
```

---

## 🚀 Try It Out
1. Clone the repository:
```bash
git clone https://github.com/<yourusername>/ai-data-migration-validation-assistant.git
cd ai-data-migration-validation-assistant
```
2. Install dependencies:
```bash
pip install pandas
```
3. Run the validation script:
```bash
python validation_agent.py
```
4. Check the output summary:
- Printed in console  
- JSON report saved in `output/validation_summary.txt`

---

## 🔮 Future Work / AWS Integration
- Replace mock AI summaries with **Amazon Bedrock** for real natural-language reporting  
- Automate **Lambda triggers** for new file uploads in S3  
- Add **QuickSight dashboards** for visual validation  
- Support multiple target databases (Redshift, Snowflake, etc.)

---

## 🧑‍💻 Author
**Sandhya Balakrishnan**  
Solo project for **AWS AI Hackathon 2025**
