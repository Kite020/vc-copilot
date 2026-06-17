from app.agents.market_research_agent import market_research

def market_research_node(state):

    industry = state["industry"]

    market_data = market_research(industry)

    print("\nMARKET DATA:")
    print(market_data)

    state["market_size"] = market_data["market_size"]
    state["cagr"] = market_data["cagr"]
    state["market_score"] = market_data["market_score"]
    state["market_analysis"] = f"""
    Market Size: {market_data['market_size']}
    CAGR: {market_data['cagr']}
    Market Score: {market_data['market_score']}
    """

    return state