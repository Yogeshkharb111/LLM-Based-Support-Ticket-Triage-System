"""
Prompt template for LLM-powered ticket triage.
This prompt enforces structured output and explainable AI decisions.
"""


def build_ticket_triage_prompt(ticket_text: str) -> str:
    """
    Builds a structured prompt for analyzing a support ticket.
    Forces JSON output with category, priority, extracted fields,
    and reasoning.
    """

    prompt = f"""
You are a senior customer support AI system responsible for ticket triage.

Your task is to analyze the support ticket below and return a STRICT JSON
object that classifies and summarizes the issue.

-------------------------
🎫 SUPPORT TICKET:
{ticket_text}
-------------------------

## Classification Rules

### Category (choose ONE only):
- Billing → payment issues, refunds, invoices, charges
- Technical → bugs, crashes, errors, performance issues
- Account → login issues, password reset, account locked, profile problems
- General → general questions, how-to, feature requests
- Other → anything that does not clearly fit above

### Priority (choose ONE only):
- Low → informational or minor issue, no urgency
- Medium → issue affects usage but has a workaround
- High → issue blocks important functionality
- Critical → system down, payment failure, security risk, severe business impact

## Information Extraction Requirements
Extract and include:
- issue_summary → one concise sentence summarizing the problem
- impacted_module → product, feature, or module affected (or "Unknown")
- urgency_indicators → list of words or phrases that indicate urgency

## Suggested Action
Provide a clear next step for the support team.

## Output Requirements (VERY IMPORTANT)
- Output ONLY valid JSON
- Do NOT include markdown, comments, or explanations outside JSON
- Use empty string "" or empty list [] if information is missing
- Be conservative: do not assume facts not stated in the ticket

## JSON Schema (Must Match Exactly)

{{
  "category": "",
  "priority": "",
  "issue_summary": "",
  "impacted_module": "",
  "urgency_indicators": [],
  "suggested_next_action": "",
  "reasoning": ""
}}

Ensure your response strictly follows this schema.
"""

    return prompt.strip()
