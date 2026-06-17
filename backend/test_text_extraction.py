import fitz

doc = fitz.open(
    "pitch_decks/Pitch-Deck-airbnb.pdf"
)

print("Pages:", len(doc))

for i in range(min(3, len(doc))):

    page = doc[i]

    images = page.get_images()

    print(
        f"Page {i+1}:",
        len(images),
        "images"
    )