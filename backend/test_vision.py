from app.services.vision_service import (
    pdf_to_images
)

images = pdf_to_images(
    "pitch_decks/Pitch-Deck-airbnb.pdf"
)

print(
    "Pages:",
    len(images)
)

images[0].save(
    "first_page.png"
)