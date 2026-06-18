from app.llm import llm
from app.llms.gemini_client import gemini_llm


def invoke_llm(prompt):

    try:

        print(
            "\nUsing OpenRouter...\n"
        )

        response = llm.invoke(
            prompt
        )

        return response

    except Exception as e:

        print(
            "\nOpenRouter Failed\n"
        )

        print(e)

        print(
            "\nSwitching to Gemini...\n"
        )

        response = gemini_llm.invoke(
            prompt
        )

        return response