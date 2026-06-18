import os
import json

from dotenv import load_dotenv
from tavily import TavilyClient
from app.llms.fallback_llm import invoke_llm
from app.small_llm import small_llm

tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def market_research(industry):

    search_query = f"{industry} market size growth rate trends"

    search_results = tavily.search(
        query=search_query,
        max_results=3
    )

    evidence = ""

    for result in search_results["results"]:
        evidence += f"""
Title: {result['title']}

Content:
{result['content']}

Source:
{result['url']}

------------------------
"""

    prompt = f"""
You are a Venture Capital market analyst.

Industry:
{industry}

Based on the market research evidence provided below:

{evidence}

Return ONLY valid JSON.

Format:

{{
    "market_size": "",
    "cagr": "",
    "market_score": 0
}}

Rules:

- market_size should be the estimated market size.
- cagr should be the growth rate.
- market_score must be an integer from 1-10.
- Return JSON only.
"""

    response = small_llm.invoke(prompt)

    cleaned = response.content
    cleaned = cleaned.replace("```json", "")
    cleaned = cleaned.replace("```", "")
    cleaned = cleaned.strip()

    print("\nMARKET EXTRACTION:\n")
    print(cleaned)

    return json.loads(cleaned)