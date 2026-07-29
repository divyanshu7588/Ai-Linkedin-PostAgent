import smtplib
from email.mime.text import MIMEText
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, RECEIVER_EMAIL


def send_email(post):

    # Safety check
    if isinstance(post, list):
        post = "\n".join(map(str, post))
    else:
        post = str(post)

    msg = MIMEText(post, "plain", "utf-8")
    msg["Subject"] = "Today's LinkedIn Post"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = RECEIVER_EMAIL

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

    print("✅ Email Sent Successfully")