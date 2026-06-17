import os

from app.utils.pdf_to_images import convert_pdf_to_images

pdfs = [
    f for f in os.listdir("pitch_decks")
    if f.endswith(".pdf")
]

pdf_path = f"pitch_decks/{pdfs[0]}"

print("Using:", pdf_path)

images = convert_pdf_to_images(pdf_path)

print(images)