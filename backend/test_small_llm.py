from app.small_llm import small_llm

response = small_llm.invoke(
    "What is 2 + 2?"
)

print(response.content)