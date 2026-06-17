from fastapi import FastAPI
from app.routes.upload import router as upload_router

app = FastAPI(
    title="VentureMind AI",
    version="1.0.0"
)

app.include_router(upload_router)

@app.get("/")
def home():
    return {"message": "VentureMind AI Backend Running"}