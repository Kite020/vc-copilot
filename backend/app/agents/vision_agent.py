import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def analyze_slide(image_path):

    uploaded_file = client.files.upload(
        file=image_path
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            uploaded_file,
            """
You are a Venture Capital analyst.

Analyze this pitch deck slide.

Extract:

1. Slide Type
2. Key Information
3. Important Numbers
4. Startup Signals

Return concise structured text.
"""
        ]
    )

    return response.text