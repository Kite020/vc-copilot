from app.agents.deck_extraction_agent import (
    extract_startup_info
)

with open(
    "deck_analysis.txt",
    "r"
) as f:

    deck_analysis = f.read()

result = extract_startup_info(
    deck_analysis
)

print(result)