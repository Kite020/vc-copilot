from fastapi import APIRouter, UploadFile, File
import os

from app.services.pdf_service import extract_pdf_text

router = APIRouter()

UPLOAD_DIR = "pitch_decks"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_pitch_deck(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_pdf_text(file_path)

    return {
        "filename": file.filename,
        "characters_extracted": len(text),
        "preview": text[:1000]
    }