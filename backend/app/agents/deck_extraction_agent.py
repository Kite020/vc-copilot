
import json

from app.llm import llm


def extract_startup_info(deck_text):

    prompt = f"""
You are a Venture Capital analyst.

Analyze the startup information below and extract the details.

Return ONLY valid JSON.

Required JSON format:

{{
    "startup_name": "",
    "industry": "",
    "problem": "",
    "solution": "",
    "business_model": "",
    "target_market": "",
    "funding_stage": "",
    "founders": []
}}

Startup Information:

{deck_text}
"""

    response = llm.invoke(prompt)

    cleaned = response.content

    cleaned = cleaned.replace("```json", "")
    cleaned = cleaned.replace("```", "")
    cleaned = cleaned.strip()

    return json.loads(cleaned)