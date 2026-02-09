def format_output(fields, missing_fields, route, reason):
    return {
        "extractedFields": fields,
        "missingFields": missing_fields,
        "recommendedRoute": route,
        "reasoning": reason
    }
