from app.agents.founder_agent import (
    founder_analysis
)


def founder_node(state):

    print("\n=== FOUNDER NODE EXECUTING ===\n")

    data = founder_analysis(
        state["founders"]
    )

    print("\nFOUNDER DATA:")
    print(data)

    state["founder_score"] = (
        data["founder_score"]
    )

    state["founder_strengths"] = (
        data["founder_strengths"]
    )

    state["founder_risks"] = (
        data["founder_risks"]
    )

    return state