import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

from config import EMAIL_ADDRESS, EMAIL_PASSWORD, RECEIVER_EMAIL


def send_email(post, image_path):

    msg = MIMEMultipart()

    msg["Subject"] = "Today's LinkedIn Post"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = RECEIVER_EMAIL

    body = MIMEText(post, "plain", "utf-8")
    msg.attach(body)

    with open(image_path, "rb") as f:
        img = MIMEImage(f.read())
        img.add_header(
            "Content-Disposition",
            "attachment",
            filename="linkedin.png"
        )
        msg.attach(img)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

    print("✅ Email Sent Successfully")