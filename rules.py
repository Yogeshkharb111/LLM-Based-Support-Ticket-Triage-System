"""
Rule-based logic to override or reinforce LLM-assigned priority.

This module adds determinism and safety to the AI system by ensuring
that critical issues are never under-prioritized due to LLM errors
or ambiguity.
"""

from typing import Dict, List


# -----------------------------
# Priority Keyword Definitions
# -----------------------------

CRITICAL_KEYWORDS: List[str] = [
    "system down",
    "service unavailable",
    "payment failed multiple times",
    "charged twice",
    "security breach",
    "data loss"
]

HIGH_KEYWORDS: List[str] = [
    "unable to login",
    "account locked",
    "error",
    "crash",
    "checkout failed"
]


# -----------------------------
# Rule Engine
# -----------------------------

def apply_priority_rules(llm_output: Dict, ticket_text: str) -> Dict:
    """
    Applies rule-based priority overrides based on keywords found in:
    - raw ticket text (source of truth)
    - issue_summary
    - urgency_indicators

    Rule precedence:
    1. Critical overrides
    2. High overrides
    3. No override (LLM priority retained)

    Args:
        llm_output (dict): Structured output from LLM or mock response
        ticket_text (str): Original user-submitted ticket text

    Returns:
        dict: Updated output with final priority and reasoning
    """

    if not isinstance(llm_output, dict):
        raise ValueError("LLM output must be a dictionary")

    if not isinstance(ticket_text, str):
        raise ValueError("ticket_text must be a string")

    # Ensure required fields exist
    llm_output.setdefault("priority", "Medium")
    llm_output.setdefault("issue_summary", "")
    llm_output.setdefault("urgency_indicators", [])
    llm_output.setdefault("reasoning", "")

    # Normalize text for scanning (IMPORTANT FIX)
    text_to_scan = " ".join([
        ticket_text,
        llm_output.get("issue_summary", ""),
        " ".join(llm_output.get("urgency_indicators", []))
    ]).lower()

    original_priority = llm_output["priority"]

    # -----------------------------
    # Apply Critical Rules
    # -----------------------------
    for keyword in CRITICAL_KEYWORDS:
        if keyword in text_to_scan:
            llm_output["priority"] = "Critical"
            llm_output["reasoning"] += (
                f" Rule-based override applied due to critical keyword: '{keyword}'."
            )
            return llm_output

    # -----------------------------
    # Apply High Rules
    # -----------------------------
    for keyword in HIGH_KEYWORDS:
        if keyword in text_to_scan:
            llm_output["priority"] = "High"
            llm_output["reasoning"] += (
                f" Rule-based override applied due to high-priority keyword: '{keyword}'."
            )
            return llm_output

    # -----------------------------
    # No Override Applied
    # -----------------------------
    llm_output["priority"] = original_priority
    llm_output["reasoning"] += (
        " No rule-based priority override was required."
    )

    return llm_output
