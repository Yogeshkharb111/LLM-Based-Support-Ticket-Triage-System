import argparse
import sys

from llm_client import analyze_ticket_with_llm, mock_llm_response
from rules import apply_priority_rules
from utils import validate_llm_output, pretty_print_json


def process_ticket(ticket_text: str) -> dict:
    """
    Full ticket triage pipeline:
    1. Send ticket to LLM (or mock fallback)
    2. Validate structured output
    3. Apply rule-based priority overrides
    4. Return final result
    """

    try:
        # Step 1: Call LLM
        llm_response = analyze_ticket_with_llm(ticket_text)

    except Exception:
        # Fallback to mock response if LLM fails
        llm_response = mock_llm_response(ticket_text)

    # Step 2: Validate LLM output
    validated_output = validate_llm_output(llm_response)

    # Step 3: Apply rule-based priority overrides
    final_output = apply_priority_rules(validated_output, ticket_text)


    return final_output


def main():
    parser = argparse.ArgumentParser(
        description="LLM-powered Ticket Triage System"
    )
    parser.add_argument(
        "--ticket",
        type=str,
        required=True,
        help="Support ticket text"
    )

    args = parser.parse_args()
    ticket_text = args.ticket.strip()

    if not ticket_text:
        print("❌ Error: Ticket text cannot be empty.")
        sys.exit(1)

    try:
        result = process_ticket(ticket_text)
        pretty_print_json(result)

    except Exception as e:
        print("❌ Failed to process ticket")
        print(str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
