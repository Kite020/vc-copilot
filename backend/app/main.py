from fastapi import FastAPI, UploadFile, File
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware

from app.agents.pitch_deck_agent import process_pitch_deck
from app.utils.state_builder import build_state
from app.graph.vc_graph import graph

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "VC Copilot API Running"
    }

@app.post("/analyze-deck")
async def analyze_deck(
    file: UploadFile = File(...)
):

    return {
        "startup_name": "Airbnb",
        "recommendation": "INVEST",
        "investment_score": 90,
        "overall_risk": 2.8,
        "founder_score": 9,
        "competitors": [
            "HomeExchange",
            "Kindred"
        ]
    }


# @app.post("/analyze-deck")
# async def analyze_deck(
#     file: UploadFile = File(...)
# ):

#     os.makedirs(
#         "uploaded_decks",
#         exist_ok=True
#     )

#     pdf_path = f"uploaded_decks/{file.filename}"

#     with open(pdf_path, "wb") as buffer:
#         shutil.copyfileobj(
#             file.file,
#             buffer
#         )

#     startup = process_pitch_deck(
#         pdf_path
#     )

#     state = build_state(
#         startup
#     )

#     result = graph.invoke(
#         state
#     )

#     return {
#         "startup_name":
#         startup["startup_name"],

#         "recommendation":
#         result["recommendation"],

#         "investment_score":
#         result["investment_score"],

#         "overall_risk":
#         result["overall_risk"]
#     }