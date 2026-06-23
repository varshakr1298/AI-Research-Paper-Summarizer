from openai import OpenAI

from .config import (
    MODEL_NAME,
    OLLAMA_API_KEY,
    OLLAMA_BASE_URL
)
from .prompts import SYSTEM_PROMPT

client = OpenAI(
    base_url=OLLAMA_BASE_URL,
    api_key=OLLAMA_API_KEY
)


def summarize(
    title: str,
    content: str
) -> str:
    user_prompt = f"""
Research Paper Title:
{title}

Paper Content:
{content}

Generate an approximately
500-word Markdown summary.
"""

    response = (
        client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            temperature=0.3
        )
    )

    return (
        response
        .choices[0]
        .message
        .content
    )