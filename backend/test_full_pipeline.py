from app.graph.vc_graph import graph

from app.agents.pitch_deck_agent import (
    process_pitch_deck
)

from app.utils.state_builder import (
    build_state
)

startup = process_pitch_deck(
    "pitch_decks/Pitch-Deck-airbnb.pdf"
)

state = build_state(
    startup
)

print("\nSTATE BUILT\n")
print(state)

result = graph.invoke(
    state
)

print("\nFINAL RESULT\n")

print(
    "Recommendation:",
    result["recommendation"]
)

print(
    "Investment Score:",
    result["investment_score"]
)

print(
    "Overall Risk:",
    result["overall_risk"]
)