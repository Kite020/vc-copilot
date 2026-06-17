from app.agents.competitor_agent import (
    competitor_analysis
)

def competitor_node(state):

    print("\n=== COMPETITOR NODE EXECUTING ===\n")

    analysis = competitor_analysis(
        state["industry"],
        state["solution"]
    )

    print("\nCOMPETITOR DATA:")
    print(analysis)

    state["competitors"] = (
        analysis["top_competitors"]
    )

    state["competition_intensity"] = (
        analysis["competition_intensity"]
    )

    # Temporary compatibility layer
    state["competitor_analysis"] = f"""
Competitors:
{', '.join(analysis['top_competitors'])}

Competition Intensity:
{analysis['competition_intensity']}
"""

    return state