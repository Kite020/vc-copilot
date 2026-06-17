from app.agents.risk_agent import assess_risk


def risk_node(state):

    print("\n=== RISK NODE EXECUTING ===\n")

    risk_data = assess_risk(state)
    print("\nRISK DATA:")
    print(risk_data)

    state["market_risk"] = risk_data["market_risk"]
    state["competition_risk"] = risk_data["competition_risk"]
    state["execution_risk"] = risk_data["execution_risk"]
    state["funding_risk"] = risk_data["funding_risk"]
    state["founder_risk"] = (
        risk_data["founder_risk"]
    )

    overall_risk = (
        risk_data["market_risk"] * 0.15 +
        risk_data["competition_risk"] * 0.25 +
        risk_data["execution_risk"] * 0.30 +
        risk_data["funding_risk"] * 0.15 +
        risk_data["founder_risk"] * 0.15
    )

    state["overall_risk"] = round(
        overall_risk,
        2
    )

    state["risk_analysis"] = risk_data["summary"]

    return state