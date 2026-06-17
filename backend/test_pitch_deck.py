from app.agents.pitch_deck_agent import (
    process_pitch_deck
)

result = process_pitch_deck(
    "pitch_decks/Pitch-Deck-airbnb.pdf"
)

print("\nSTARTUP INFO\n")

print(result)