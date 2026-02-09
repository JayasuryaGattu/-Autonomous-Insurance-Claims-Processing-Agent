from ingestion.document_loader import load_document
from extraction.field_extractor import extract_fields
from validation.field_validator import find_missing_fields
from routing.claim_router import determine_route
from explanation.reasoning_generator import generate_reason
from output.json_formatter import format_output

import os
import json
import sys

def process_claim(file_path: str):
    text = load_document(file_path)
    fields = extract_fields(text)
    missing_fields = find_missing_fields(fields)
    route = determine_route(fields, missing_fields)
    reason = generate_reason(route, fields, missing_fields)
    return format_output(fields, missing_fields, route, reason)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    result = process_claim(file_path)

    # ALWAYS save outputs next to main.py (no path confusion)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_file = os.path.join(OUTPUT_DIR, f"{base_name}_output.json")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Output saved to {output_file}")


