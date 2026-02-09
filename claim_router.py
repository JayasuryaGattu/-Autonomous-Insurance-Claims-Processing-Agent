FRAUD_KEYWORDS = ["fraud", "staged", "inconsistent"]

def determine_route(fields: dict, missing_fields: list) -> str:
    description = (fields.get("description") or "").lower()

    if missing_fields:
        return "Manual Review"

    if any(word in description for word in FRAUD_KEYWORDS):
        return "Investigation Flag"

    if fields.get("claim_type") == "injury":
        return "Specialist Queue"

    if fields.get("estimated_damage", 0) < 25000:
        return "Fast-track"

    return "Manual Review"
