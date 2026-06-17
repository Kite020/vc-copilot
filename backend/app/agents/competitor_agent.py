import os
import json

from dotenv import load_dotenv
from tavily import TavilyClient

from app.llm import llm
from app.small_llm import small_llm

load_dotenv()

tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def competitor_analysis(
    industry,
    solution
):

    query = f"""
Top competitors in {industry}
providing solutions similar to:
{solution}
"""

    results = tavily.search(
        query=query,
        max_results=3
    )

    evidence = ""

    for result in results["results"]:
        evidence += f"""
Title:
{result['title']}

Content:
{result['content']}

Source:
{result['url']}

------------------------
"""

    prompt = f"""
You are a Venture Capital analyst.

Based on the evidence below:

{evidence}

Identify:

1. Top competitors
2. Competition intensity

Return ONLY valid JSON.

Format:

{{
    "top_competitors": [],
    "competition_intensity": 0
}}

Rules:

- top_competitors should contain competitor names only
- competition_intensity must be an integer from 1-10
- Return JSON only
"""

    response = small_llm.invoke(prompt)

    cleaned = response.content
    cleaned = cleaned.replace("```json", "")
    cleaned = cleaned.replace("```", "")
    cleaned = cleaned.strip()

    return json.loads(cleaned)