from app.graph.vc_graph import graph

sample_text = """
Startup Name: MediScan AI

Industry: Healthcare AI

Problem:
Hospitals spend significant time manually reviewing radiology reports.

Solution:
AI-generated preliminary reports.

Business Model:
Subscription SaaS.

Target Market:
Hospitals.

Funding Stage:
Seed.

Founders:
Dr Sarah Johnson.
Alex Chen.
"""

initial_state = {
    "raw_deck_text": sample_text
}

result = graph.invoke(initial_state)

print("\nOVERALL RISK")
print(result["overall_risk"])

print("\nRISK ANALYSIS")
print(result["risk_analysis"])

print("\nINVESTMENT SCORE")
print(result["investment_score"])

print("\nRECOMMENDATION")
print(result["recommendation"])

print("\nREASONS")
print(result["committee_reasons"])

print("\nNEXT STEPS")
print(result["next_steps"])