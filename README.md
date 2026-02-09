# Autonomous Insurance Claims Processing Agent

## Overview
This project implements a lightweight autonomous agent that processes **FNOL (First Notice of Loss)** documents for insurance claims.  
It extracts key claim details, validates missing information, classifies the claim, routes it to the appropriate workflow, and produces a structured JSON output with a clear explanation.

The system is modular, easy to extend, and designed for assessment and learning purposes.

---

## Project Objectives
- Extract important fields from FNOL documents (PDF or text)
- Detect missing or incomplete fields
- Classify and route claims based on extracted data
- Generate a short explanation for the routing decision
- Output results in structured JSON format

---

## Folder Structure

claims_agent/
│
├── ingestion/
│ └── document_loader.py # Loads PDF or text documents
│
├── extraction/
│ └── field_extractor.py # Extracts claim-related fields
│
├── validation/
│ └── field_validator.py # Identifies missing fields
│
├── routing/
│ └── claim_router.py # Determines claim workflow
│
├── explanation/
│ └── reasoning_generator.py # Explains routing decision
│
├── output/
│ └── json_formatter.py # Formats final JSON output
│
├── outputs/
│ └── *_output.json # Sample generated outputs
│
├── main.py # Application entry point
├── requirements.txt
└── README.md

---

## How It Works
1. **Document Ingestion**  
   Loads FNOL documents (PDF or text).

2. **Field Extraction**  
   Extracts key insurance fields such as policy number, claim type, and incident details.

3. **Validation**  
   Checks for missing or incomplete required fields.

4. **Routing**  
   Routes the claim to the appropriate workflow based on extracted data.

5. **Explanation Generation**  
   Produces a human-readable explanation for the routing decision.

6. **Output Formatting**  
   Saves results as a structured JSON file.

