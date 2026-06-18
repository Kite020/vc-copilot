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

from app.utils.combine_slides import (
    combine_slides
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

    batch_size = 5

    for i in range(
        0,
        len(image_paths),
        batch_size
    ):

        batch = image_paths[
            i:i + batch_size
        ]

        print(
            f"Analyzing batch {i//batch_size + 1}"
        )

        combined_image = combine_slides(
            batch,
            output_path=f"batch_{i//batch_size + 1}.png"
        )

        batch_result = analyze_slide(
            combined_image
        )

        all_notes.append(
            batch_result
        )

    deck_analysis = "\n\n".join(
        all_notes
    )

    startup_info = extract_startup_info(
        deck_analysis
    )

    return startup_info