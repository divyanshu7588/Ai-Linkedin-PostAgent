from agents.llm import llm
from database.db import get_last_posts


def writer_agent(state):

    history = "\n\n".join(get_last_posts())

    prompt = f"""
You are an expert LinkedIn writer.

Today's Topic:
AI

Avoid repeating ideas from these previous posts:

{history}

Write a fresh LinkedIn post.

Requirements:

- Professional
- 200 words max
- Engaging
- End with hashtags
"""

    response = llm.invoke(prompt)

    return {
        "topic": "AI",
        "post": response.text
    }