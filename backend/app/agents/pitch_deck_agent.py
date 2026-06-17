import os

from app.utils.pdf_to_images import (
    convert_pdf_to_images
)

from app.agents.slide_analysis_agent import (
    analyze_slide
)

from app.agents.deck_extraction_agent import (
    extract_startup_info
)


def process_pitch_deck(pdf_path):

    print("\nConverting PDF to images...")

    image_paths = convert_pdf_to_images(
        pdf_path
    )

    print(
        f"Generated {len(image_paths)} slides"
    )

    all_notes = []

    for image_path in image_paths:

        print(
            f"Analyzing {image_path}..."
        )

        result = analyze_slide(
            image_path
        )

        all_notes.append(result)

    deck_analysis = "\n\n".join(
        all_notes
    )

    startup_info = extract_startup_info(
        deck_analysis
    )

    return startup_info