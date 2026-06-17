import os
import json

from dotenv import load_dotenv
from app.llm import llm



def assess_risk(state):

    prompt = f"""
You are a senior Venture Capital Partner.

Evaluate the startup below.

Startup Name:
{state['startup_name']}

Industry:
{state['industry']}

Problem:
{state['problem']}

Solution:
{state['solution']}

Funding Stage:
{state['funding_stage']}

Market Size:
{state['market_size']}

CAGR:
{state['cagr']}

Market Score:
{state['market_score']}

Competitors:
{state['competitors']}

Competition Intensity:
{state['competition_intensity']}

Founder Score:
{state["founder_score"]}

Founder Strengths:
{state["founder_strengths"]}

Founder Risks:
{state["founder_risks"]}

Return ONLY valid JSON.

Format:

{{
    "market_risk": 0,
    "competition_risk": 0,
    "execution_risk": 0,
    "funding_risk": 0,
    "founder_risk": 0,
    "summary": ""
}}

Risk scores must be between 1 and 10.

summary requirements:

- Minimum 100 words
- Explain market risk
- Explain competition risk
- Explain execution risk
- Explain founder risk
- Never return an empty summary

Founder risk should be:

1-3 = exceptional founders
4-6 = average founders
7-10 = weak or unverified founders

Do not calculate overall risk.
Only provide individual risk scores.
Return JSON only.
"""

    response = llm.invoke(prompt)

    cleaned = response.content
    cleaned = cleaned.replace("```json", "")
    cleaned = cleaned.replace("```", "")
    cleaned = cleaned.strip()

    risk_data = json.loads(cleaned)

    if (
        "summary" not in risk_data
        or not risk_data["summary"].strip()
    ):
        risk_data["summary"] = (
            "Risk summary was not generated."
        )

    return risk_data