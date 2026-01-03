# 📌 LLM-Powered Ticket Triage System

## 🔹 Overview

The **LLM-Powered Ticket Triage System** is an AI-driven customer support automation project that analyzes incoming support tickets and automatically determines:

- 📂 **Category** (Billing, Technical, Account, General, Other)
- 🚦 **Priority** (Low, Medium, High, Critical)
- 🧾 **Key information extraction**
- 🛠️ **Suggested next action**

This system simulates **real-world enterprise AI usage** by combining **Large Language Model (LLM) reasoning** with **deterministic rule-based logic** to ensure reliability, explainability, and safety.

---

## 🎯 Objective

Customer support teams spend significant manual effort reading and prioritizing tickets.

**Goal of this project:**

> Reduce manual effort and response time by automatically triaging customer support tickets using LLMs augmented with rule-based business logic.

---

## ⚙️ Key Features

- 📝 Accepts customer support tickets as **plain text input**
- 🧠 Uses an **LLM for classification and information extraction**
- 🚨 Applies **rule-based priority overrides** for critical cases
- 📦 Produces **structured JSON output**
- 🔁 Includes **mock fallback** for API quota limitations
- 💻 **CLI-based interface** (easy to test, demo, and interview-ready)

---

## 🧠 AI Concepts Demonstrated

This project showcases several important AI and system design concepts:

- Text classification
- Prompt engineering
- Workflow automation
- Hybrid AI systems (LLM + rules)
- Explainable AI decisions
- Structured outputs (JSON schemas)
- Fail-safe design for production systems

---

## 🏗️ System Architecture

### High-Level Flow

```text
User
  ↓
CLI Interface (main.py)
  ↓
LLM Client (llm_client.py)
  ↓
OpenAI LLM
  ↓
Validation Layer (utils.py)
  ↓
Rule Engine (rules.py)
  ↓
Structured JSON Output


```



```
ticket_triage/
│── main.py            # CLI entry point
│── llm_client.py      # OpenAI API interaction
│── prompt.py          # Prompt template
│── rules.py           # Rule-based priority logic
│── utils.py           # JSON validation & helpers
│── .env               # API key (not committed)
│── requirements.txt
│── README.md

```


## 🔑 Classification Logic

### 📂 Categories

| Category   | Description |
|-----------|-------------|
| Billing   | Payments, refunds, invoices |
| Technical | Bugs, crashes, system errors |
| Account   | Login issues, password reset, account lock |
| General  | How-to questions, feature requests |
| Other    | Uncategorized issues |

---

### 🚦 Priority Levels

| Priority  | Description |
|----------|-------------|
| Low      | Informational or minor issue |
| Medium   | Affects usage, workaround exists |
| High     | Blocks important functionality |
| Critical | Payment failure, system down, security risk |

---

## 🚨 Rule-Based Priority Overrides

To ensure **safety and correctness**, deterministic rules override LLM-generated priorities when **critical keywords** are detected.

### Examples

| Keyword / Phrase | Overridden Priority |
|-----------------|--------------------|
| "payment failed multiple times" | Critical |
| "account locked" | High |
| "system down" | Critical |
| "security breach" | Critical |

This **hybrid AI approach** prevents LLM misclassification in **high-risk scenarios**.

---

## 📤 Output Format (JSON)

```json
{
  "category": "Billing",
  "priority": "Critical",
  "issue_summary": "Payment failed multiple times and account is locked",
  "impacted_module": "Payments / Account",
  "urgency_indicators": [
    "payment failed twice",
    "account locked",
    "urgent"
  ],
  "suggested_next_action": "Escalate to billing team and verify account status",
  "reasoning": "Rule-based override applied due to critical keywords"
}



```

```
▶️ How to Run the Project

1️⃣ Create & Activate Virtual Environment (Windows)
py -m venv venv
venv\Scripts\activate

2️⃣ Install Dependencies
py -m pip install -r requirements.txt

3️⃣ Add OpenAI API Key

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here
.

4️⃣ Run the CLI
py main.py --ticket "My payment failed twice and my account is locked. This is urgent."

⚠️ API Quota Handling (Fail-Safe Design)

If the OpenAI API quota is exceeded, the system automatically switches to a mock response mode, ensuring:

✔️ Pipeline continuity

✔️ CLI remains functional

✔️ Easy demonstration during interviews or evaluations

✔️ No hard dependency on live API access

✅ Why This Project Stands Out

Real-world customer support automation use case

Hybrid AI design (LLM + deterministic rules)

Explainable and auditable decisions

Production-oriented error handling

Strong demonstration of LLM system design skills

👨‍💻 Author

Yogesh Kharb
AI / ML Engineer | LLM & Agentic Systems Enthusiast

```
