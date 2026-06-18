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
- Do not include aliases or old names.
- Example: use "Airbnb", not "AirBed&Breakfast".

- founders must contain founder names if they appear anywhere in the deck.
- Look for sections such as:
  Founder
  Founders
  Team
  Leadership
  About Us
  Management

- Return founder names only.
- Do not include job titles.
- Do not include company names.
- If founders are not mentioned, return an empty list.

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
    "founders": [
        {{
            "name": ""
        }}
    ]
}}
"""

    response = small_llm.invoke(prompt)

    cleaned = response.content
    cleaned = cleaned.replace("```json", "")
    cleaned = cleaned.replace("```", "")
    cleaned = cleaned.strip()

    print("\nEXTRACTION RESULT:\n")
    print(cleaned)

    return json.loads(cleaned)