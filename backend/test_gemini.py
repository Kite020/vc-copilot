import os
from dotenv import load_dotenv

from app.llm import llm

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

response = llm.invoke(
    "Say hello in one sentence."
)

print(response.content)