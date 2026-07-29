from apscheduler.schedulers.blocking import BlockingScheduler
from graph import graph
from agents.email import send_email


def run_agent():
    try:
        print("Generating LinkedIn Post...")

        result = graph.invoke({})

        post = result["post"]

        send_email(post)

        print("✅ Email Sent Successfully")

    except Exception as e:
        print(f"Error: {e}")


scheduler = BlockingScheduler()

# Every day at 8:00 AM
scheduler.add_job(run_agent, "interval", minutes=1)

print("Scheduler Started...")
print("Waiting for 08:00 AM...")

scheduler.start()