import re

def extract_fields(text: str) -> dict:
    fields = {}

    fields["policy_number"] = _extract_policy_number(text)
    fields["claim_type"] = _extract_claim_type(text)
    fields["estimated_damage"] = _extract_estimate(text)
    fields["description"] = _extract_description(text)

    return fields

def _extract_policy_number(text):
    match = re.search(r"POLICY NUMBER\s*[:\-]?\s*(\w+)", text, re.IGNORECASE)
    return match.group(1) if match else None

def _extract_claim_type(text):
    if "injury" in text.lower():
        return "injury"
    elif "vehicle" in text.lower():
        return "vehicle"
    return None

def _extract_estimate(text):
    match = re.search(r"ESTIMATE AMOUNT\s*[:\-]?\s*₹?\$?([\d,]+)", text, re.IGNORECASE)
    if match:
        return int(match.group(1).replace(",", ""))
    return None

def _extract_description(text):
    match = re.search(r"DESCRIPTION OF ACCIDENT(.+)", text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else None
