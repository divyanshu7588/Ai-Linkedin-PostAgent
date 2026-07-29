import os
import requests
from urllib.parse import quote


def image_agent(state):
    post = state["post"]

    prompt = f"""
Professional LinkedIn illustration.

Topic:
{post}

Requirements:
- Modern flat vector
- Blue and white theme
- AI and Technology
- Minimal
- No text
- Professional
"""

    os.makedirs("images", exist_ok=True)

    url = f"https://image.pollinations.ai/prompt/{quote(prompt)}"

    response = requests.get(url, timeout=120)
    response.raise_for_status()

    with open("images/linkedin.png", "wb") as f:
        f.write(response.content)

    return {
        "image": "images/linkedin.png"
    }