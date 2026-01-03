"""
Utility functions for validating and formatting LLM outputs.
Ensures structured, safe, and consistent JSON responses.
"""

import json
from typing import Dict, List


REQUIRED_FIELDS = {
    "category": str,
    "priority": str,
    "issue_summary": str,
    "impacted_module": str,
    "urgency_indicators": list,
    "suggested_next_action": str,
    "reasoning": str,
}

VALID_CATEGORIES = {"Billing", "Technical", "Account", "General", "Other"}
VALID_PRIORITIES = {"Low", "Medium", "High", "Critical"}


def validate_llm_output(llm_output: Dict) -> Dict:
    """
    Validates and normalizes LLM output.
    Ensures required fields exist and have correct types.

    Args:
        llm_output (dict): Raw LLM output

    Returns:
        dict: Validated and normalized output
    """

    if not isinstance(llm_output, dict):
        raise ValueError("LLM output must be a dictionary")

    validated = {}

    for field, field_type in REQUIRED_FIELDS.items():
        value = llm_output.get(field)

        # Handle missing fields
        if value is None:
            value = [] if field_type is list else ""

        # Type normalization
        if field_type is list and not isinstance(value, list):
            value = []
        elif field_type is str and not isinstance(value, str):
            value = str(value)

        validated[field] = value

    # Normalize category
    if validated["category"] not in VALID_CATEGORIES:
        validated["category"] = "Other"

    # Normalize priority
    if validated["priority"] not in VALID_PRIORITIES:
        validated["priority"] = "Medium"

    return validated


def pretty_print_json(data: Dict) -> None:
    """
    Prints JSON in a readable format for CLI output.

    Args:
        data (dict): Final structured output
    """

    print(json.dumps(data, indent=2, ensure_ascii=False))
