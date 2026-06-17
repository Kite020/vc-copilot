from app.graph.vc_graph import graph
from app.agents.memo_agent import generate_memo

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
Dr Sarah Johnson
Alex Chen
"""

initial_state = {
    "raw_deck_text": sample_text
}

result = graph.invoke(initial_state)

memo = generate_memo(result)
from app.utils.pdf_generator import (
    generate_pdf
)

generate_pdf(
    memo,
    "data/reports/investment_memo.pdf"
)

with open(
    "data/reports/memo.txt",
    "w"
) as f:
    f.write(memo)

print("\n")
print("=" * 80)
print("VC INVESTMENT MEMO")
print("=" * 80)
print("\n")

print(memo)