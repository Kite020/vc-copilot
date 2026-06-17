import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

small_llm = ChatOpenAI(
    model="qwen/qwen3-8b",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0
)