from datetime import datetime

from graph import graph
from agents.email import send_email
from database.db import save_post

result = graph.invoke({})

send_email(
    result["post"],
    result["image"]
)

save_post(
    date=datetime.now().strftime("%Y-%m-%d"),
    topic=result["topic"],
    post=result["post"],
    image=result["image"]
)

print("✅ Saved to Database")