from langgraph.graph import StateGraph
from langgraph.graph import END

from app.models.state import VCState

from app.agents.market_research_node import market_research_node
from app.agents.competitor_node import competitor_node
from app.agents.risk_node import risk_node
from app.agents.committee_node import committee_node
from app.agents.founder_node import (
    founder_node
)

builder = StateGraph(VCState)

builder.add_node(
    "market_research",
    market_research_node
)

builder.add_node(
    "competitor_analysis",
    competitor_node
)

builder.add_node(
    "risk_assessment",
    risk_node
)

builder.add_node(
    "committee",
    committee_node
)

builder.add_node(
    "founder_analysis",
    founder_node
)

builder.set_entry_point(
    "market_research"
)

builder.add_edge(
    "market_research",
    "competitor_analysis"
)

builder.add_edge(
    "competitor_analysis",
    "founder_analysis"
)

builder.add_edge(
    "founder_analysis",
    "risk_assessment"
)

builder.add_edge(
    "risk_assessment",
    "committee"
)

builder.add_edge(
    "committee",
    END
)

graph = builder.compile()