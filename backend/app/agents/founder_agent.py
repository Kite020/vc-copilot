import os
import json

from tavily import TavilyClient

from app.small_llm import small_llm


tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def founder_analysis(founders):

    founder_text = ", ".join(founders)

    query = f"""
Background information about founders:
{founder_text}

Experience
Education
Previous startups
Achievements
"""

    results = tavily.search(
        query=query,
        max_results=3
    )

    # No search results found
    if len(results["results"]) == 0:
        return {
            "founder_score": 5,
            "founder_verified": False,
            "founder_strengths": [
                "Founder background could not be verified",
                "Limited public information available",
                "Additional diligence required"
            ],
            "founder_risks": [
                "Insufficient public information available",
                "Founder identity could not be verified",
                "Background verification required"
            ]
        }

    evidence = ""

    for result in results["results"]:

        evidence += f"""

Title:
{result['title']}

Content:
{result['content']}

Source:
{result['url']}

------------------
"""

    prompt = f"""
You are a Venture Capital Partner.

Analyze the founders using ONLY the evidence below.

IMPORTANT RULES:

- Use ONLY information present in the evidence.
- Do NOT infer education.
- Do NOT infer work history.
- Do NOT infer startup experience.
- Do NOT infer professional connections.
- Do NOT infer achievements.
- If information is missing, explicitly state that it could not be verified.
- Never fabricate founder credentials.
- Never use information from unrelated people with similar names.

Evidence:

{evidence}

Return ONLY valid JSON.

Format:

{{
    "founder_score": 0,
    "founder_verified": false,
    "founder_strengths": [],
    "founder_risks": []
}}

Rules:

- founder_score must be between 1 and 10
- founder_verified must be true or false
- exactly 3 strengths
- exactly 3 risks
- return JSON only

If founder identity cannot be confidently verified:

founder_verified = false

founder_score = 5

founder_strengths = [
    "Founder background could not be verified",
    "Limited public information available",
    "Additional diligence required"
]

founder_risks = [
    "Insufficient public information available",
    "Founder identity could not be verified",
    "Background verification required"
]
"""

    response = small_llm.invoke(prompt)

    cleaned = response.content
    cleaned = cleaned.replace("```json", "")
    cleaned = cleaned.replace("```", "")
    cleaned = cleaned.strip()

    founder_data = json.loads(cleaned)

    # Safety fallback to prevent hallucinated founder information
    if founder_data.get("founder_verified") is False:

        founder_data["founder_score"] = 5

        founder_data["founder_strengths"] = [
            "Founder background could not be verified",
            "Limited public information available",
            "Additional diligence required"
        ]

        founder_data["founder_risks"] = [
            "Insufficient public information available",
            "Founder identity could not be verified",
            "Background verification required"
        ]

    return founder_data