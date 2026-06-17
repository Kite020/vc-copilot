import base64

from app.small_llm import small_llm

with open("slide_1.png", "rb") as f:
    image_base64 = base64.b64encode(
        f.read()
    ).decode()

response = small_llm.invoke(
    [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Describe this startup pitch deck slide."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{image_base64}"
                    }
                }
            ]
        }
    ]
)

print(response.content)