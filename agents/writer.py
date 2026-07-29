from agents.llm import llm

def writer(state):
    topic = state["topic"]

    response = llm.invoke(
        f"""
        Write a professional LinkedIn post on {topic}.

        Keep it engaging.
        """
    )

    return {
        "post": response.content
    }