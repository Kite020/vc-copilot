import os

from app.agents.slide_analysis_agent import (
    analyze_slide
)

slides = sorted(
    [
        f for f in os.listdir(".")
        if f.startswith("slide_")
        and f.endswith(".png")
    ],
    key=lambda x: int(
        x.replace("slide_", "")
         .replace(".png", "")
    )
)

all_notes = []

for slide in slides:

    print(f"\nAnalyzing {slide}...")

    result = analyze_slide(slide)

    all_notes.append(
        f"""
SLIDE: {slide}

{result}
"""
    )

with open(
    "deck_analysis.txt",
    "w"
) as f:

    f.write(
        "\n".join(all_notes)
    )

print(
    "\nSaved to deck_analysis.txt"
)