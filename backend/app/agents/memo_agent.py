from app.llm import llm


def generate_memo(state):

    prompt = f"""
You are a Venture Capital Partner.

Create a professional investment memo.

Startup:
{state['startup_name']}

Industry:
{state['industry']}

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

Overall Risk:
{state['overall_risk']}

Investment Score:
{state['investment_score']}

Recommendation:
{state['recommendation']}

Reasons:
{state['committee_reasons']}

Generate a professional Venture Capital Investment Memo.

Format:

# Executive Summary

# Startup Overview

# Market Opportunity

# Competitive Landscape

# Key Risks

# Investment Recommendation

Requirements:

- Professional VC tone
- Use concrete facts from the analysis
- Explain reasoning clearly
- 500-800 words

Include:

1. Executive Summary
2. Market Opportunity
3. Competitive Landscape
4. Risks
5. Investment Recommendation
"""

    response = llm.invoke(prompt)

    return response.content