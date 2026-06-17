import json

from app.small_llm import small_llm


def extract_startup_info(deck_analysis):

    prompt = f"""
You are a Venture Capital analyst.

Below is the analysis of an entire startup pitch deck.

{deck_analysis}

Extract the startup information.

Rules:
- startup_name should contain ONLY the current company name.
- Do not include aliases or old names in startup_name.
- Example: use "Airbnb", not "Airbnb (AirBed&Breakfast)".

Return ONLY valid JSON.

Format:

{{
    "startup_name": "",
    "industry": "",
    "problem": "",
    "solution": "",
    "business_model": "",
    "market": "",
    "traction": "",
    "founders": []
}}
"""

    response = small_llm.invoke(prompt)

    cleaned = response.content
    cleaned = cleaned.replace("```json", "")
    cleaned = cleaned.replace("```", "")
    cleaned = cleaned.strip()

    return json.loads(cleaned)