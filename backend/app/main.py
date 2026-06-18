from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil

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


@app.get("/download-memo")
def download_memo():

    return FileResponse(
        path="data/reports/investment_memo.pdf",
        filename="investment_memo.pdf",
        media_type="application/pdf"
    )


@app.post("/analyze-deck")
async def analyze_deck(
    file: UploadFile = File(...)
):

    try:

        os.makedirs(
            "uploaded_decks",
            exist_ok=True
        )

        pdf_path = (
            f"uploaded_decks/{file.filename}"
        )

        with open(
            pdf_path,
            "wb"
        ) as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        print(
            "\nProcessing Pitch Deck...\n"
        )

        startup = process_pitch_deck(
            pdf_path
        )

        print(
            "\nStartup Extracted:\n"
        )

        print(startup)

        state = build_state(
            startup
        )

        result = graph.invoke(
            state
        )

        return {
            "startup_name":
            result["startup_name"],

            "startup_summary":
            (
                f"{result['startup_name']} operates "
                f"in the {result['industry']} industry. "
                f"It solves {result['problem']} "
                f"through {result['solution']}."
            ),

            "recommendation":
            result["recommendation"],

            "investment_score":
            result["investment_score"],

            "overall_risk":
            result["overall_risk"],

            "founder_score":
            result["founder_score"],

            "competitors":
            result["competitors"],

            "founder_strengths":
            result["founder_strengths"],

            "founder_risks":
            result["founder_risks"],

            "reasons":
            result["committee_reasons"],

            "next_steps":
            result["next_steps"],

            "risk_summary":
            result["risk_analysis"],

            "market_risk":
            result["market_risk"],

            "competition_risk":
            result["competition_risk"],

            "execution_risk":
            result["execution_risk"],

            "funding_risk":
            result["funding_risk"],

            "founder_risk":
            result["founder_risk"]
        }

    except Exception as e:

        print(
            "\nERROR:\n",
            str(e)
        )

        return {
            "success": False,
            "error": str(e)
        }