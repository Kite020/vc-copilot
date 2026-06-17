from app.agents.investment_committee_agent import (
    committee_decision
)

def committee_node(state):

    print("\n=== COMMITTEE NODE EXECUTING ===\n")

    result = committee_decision(state)

    state["investment_score"] = result[
        "investment_score"
    ]

    state["recommendation"] = result[
        "recommendation"
    ]

    state["committee_reasons"] = result[
        "reasons"
    ]

    state["next_steps"] = result[
        "next_steps"
    ]

    return state