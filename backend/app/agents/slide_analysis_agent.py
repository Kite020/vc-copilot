import base64

from app.small_llm import small_llm


def analyze_slide(image_path):

    with open(image_path, "rb") as f:
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
                        "text": """
You are a Senior Venture Capital analyst.

Analyze these pitch deck slides.

For EACH slide identify:

- Slide Type
- Key Information
- Important Numbers
- Founders Mentioned
- Competitors Mentioned
- Traction Mentioned
- Revenue Mentioned
- Market Information
- Startup Insights

IMPORTANT:

- Mention founder names exactly if visible.
- Mention competitor names exactly if visible.
- Mention revenue and growth metrics exactly if visible.
- Do not hallucinate.
- If information is missing, say "Not Mentioned".

Return a structured summary of all slides.

Keep response under 150 words.
"""
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

    return response.content