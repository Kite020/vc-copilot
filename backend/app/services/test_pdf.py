from pypdf import PdfReader

reader = PdfReader("pitch_decks/Pitch-Deck-airbnb.pdf")

print("Pages:", len(reader.pages))

for i, page in enumerate(reader.pages):
    print(f"\nPage {i+1}")
    print(repr(page.extract_text()))