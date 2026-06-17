from typing import TypedDict


class VCState(TypedDict):

    # Input
    raw_deck_text: str

    # Extraction Agent
    startup_name: str
    industry: str
    problem: str
    solution: str
    business_model: str
    target_market: str
    funding_stage: str
    founders: list

    # Market Agent
    market_size: str
    cagr: str
    market_score: int
    market_analysis: str

    # Competitor Agent
    competitors: list
    competition_intensity: int
    competitor_analysis: str


    # Risk Agent
    market_risk: int
    competition_risk: int
    execution_risk: int
    funding_risk: int
    overall_risk: float
    risk_analysis: str

    # Committee Agent
    investment_score: int
    recommendation: str
    committee_reasons: list
    next_steps: list

    founder_verified: bool
    founder_score: int
    founder_strengths: list
    founder_risk: int
    founder_risks: list