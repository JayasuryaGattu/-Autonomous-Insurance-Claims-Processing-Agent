def generate_reason(route: str, fields: dict, missing_fields: list) -> str:
    if missing_fields:
        return f"Routed to Manual Review because missing fields: {', '.join(missing_fields)}."

    if route == "Investigation Flag":
        return "Keywords indicating possible fraud were found in the description."

    if route == "Specialist Queue":
        return "Claim involves injury and requires specialist handling."

    if route == "Fast-track":
        return "Estimated damage is below ₹25,000 and all mandatory fields are present."

    return "Claim routed based on default rules."
