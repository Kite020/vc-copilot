import json
from app.agents.deck_extraction_agent import extract_startup_info

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

result = extract_startup_info(sample_text)

print(json.dumps(result, indent=4))