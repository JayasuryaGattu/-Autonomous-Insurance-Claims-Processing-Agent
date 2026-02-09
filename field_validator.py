MANDATORY_FIELDS = [
    "policy_number",
    "claim_type",
    "estimated_damage"
]

def find_missing_fields(fields: dict) -> list:
    missing = []
    for field in MANDATORY_FIELDS:
        if not fields.get(field):
            missing.append(field)
    return missing
