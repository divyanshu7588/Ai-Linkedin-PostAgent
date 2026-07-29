from agents.llm import llm


def writer_agent(state):
    prompt = """
    You are an expert LinkedIn content writer.

    Write ONE professional LinkedIn post.

    Rules:
    - Domain must be either Artificial Intelligence or Cyber Security.
    - Choose the topic yourself.
    - Keep it between 180 and 250 words.
    - Start with a strong hook.
    - Use simple and natural English.
    - Write like an experienced software engineer sharing knowledge.
    - Do NOT use emojis.
    - End with a thoughtful question.
    - Add 5 relevant hashtags.
    - Return ONLY the LinkedIn post.
    """

    response = llm.invoke(prompt)

    # Always convert response to string
    post = response.text() if hasattr(response, "text") else str(response.content)

    return {
        "post": response.text
    }