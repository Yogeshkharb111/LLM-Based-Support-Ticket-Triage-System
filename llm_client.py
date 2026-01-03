"""
LLM client module.

Handles interaction with the OpenAI API and provides
a mock fallback response when API quota is exceeded
or API access is unavailable.
"""

from typing import Dict
import os


# ----------------------------------
# REAL LLM CALL (SIMULATED / OPTIONAL)
# ----------------------------------

def analyze_ticket_with_llm(ticket: str) -> Dict:
    """
    Sends the ticket to the LLM and returns structured output.

    NOTE:
    - If API key is missing or quota is exceeded,
      this function raises an exception.
    - main.py will automatically fall back to mock_llm_response().

    Args:
        ticket (str): Raw support ticket text

    Returns:
        dict: Structured LLM response
    """

    api_key = os.getenv("OPENAI_API_KEY")

    # Simulate API failure if key is missing
    if not api_key:
        raise RuntimeError("OpenAI API key not found or quota exceeded")

    # 👉 PLACEHOLDER for real OpenAI call
    # (You can integrate OpenAI/Gemini later)

    raise RuntimeError("Simulated API quota exceeded")


# ----------------------------------
# MOCK LLM FALLBACK
# ----------------------------------

def mock_llm_response(ticket: str) -> Dict:
    """
    Generates a mock LLM response based on keyword heuristics.
    Used when the real LLM is unavailable.
    """

    ticket_lower = ticket.lower()

    if "payment" in ticket_lower:
        return {
            "category": "Billing",
            "priority": "High",
            "issue_summary": "Payment related issue",
            "impacted_module": "Payments",
            "urgency_indicators": [],
            "suggested_next_action": "Check payment logs",
            "reasoning": "Mock LLM classification based on payment-related keywords."
        }

    elif "crash" in ticket_lower or "error" in ticket_lower:
        return {
            "category": "Technical",
            "priority": "High",
            "issue_summary": "Application crash issue",
            "impacted_module": "Mobile App",
            "urgency_indicators": [],
            "suggested_next_action": "Investigate app crash logs",
            "reasoning": "Mock LLM classification based on crash/error keywords."
        }

    elif "thank" in ticket_lower or "great job" in ticket_lower:
        return {
            "category": "General",
            "priority": "Low",
            "issue_summary": "User feedback",
            "impacted_module": "General",
            "urgency_indicators": [],
            "suggested_next_action": "Send appreciation response",
            "reasoning": "Mock LLM classification for non-issue feedback."
        }

    else:
        return {
            "category": "General",
            "priority": "Medium",
            "issue_summary": "General inquiry",
            "impacted_module": "Support",
            "urgency_indicators": [],
            "suggested_next_action": "Respond with help article",
            "reasoning": "Mock LLM classification for general inquiry."
        }
