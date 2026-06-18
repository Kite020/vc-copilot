import os
import json

from dotenv import load_dotenv
from app.llms.fallback_llm import invoke_llm


def committee_decision(state):

    prompt = f"""
You are the Investment Committee of a Venture Capital firm.

Startup:
{state["startup_name"]}

Industry:
{state["industry"]}

Market Size:
{state["market_size"]}

CAGR:
{state["cagr"]}

Market Score:
{state["market_score"]}

Competitors:
{state["competitors"]}

Competition Intensity:
{state["competition_intensity"]}

Market Risk:
{state["market_risk"]}

Competition Risk:
{state["competition_risk"]}

Execution Risk:
{state["execution_risk"]}

Funding Risk:
{state["funding_risk"]}

Overall Risk:
{state["overall_risk"]}

Make an investment decision.

Return ONLY valid JSON.

Format:

{{
    "investment_score": 0,
    "recommendation": "",
    "reasons": [],
    "next_steps": []
}}

Rules:

- investment_score must be between 0 and 100
- recommendation must be INVEST or DO NOT INVEST
- provide exactly 3 reasons
- provide exactly 3 next steps
- return JSON only
"""

    response = invoke_llm(prompt)

    cleaned = response.content
    cleaned = cleaned.replace("```json", "")
    cleaned = cleaned.replace("```", "")
    cleaned = cleaned.strip()

    return json.loads(cleaned)