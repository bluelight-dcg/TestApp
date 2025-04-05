
import smtplib

sender = "hello@demomailtrap.co"
receiver = "fran3ar@gmail.com"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
    server.starttls()
    server.login("api", "8a378472805926e771efbdad5411dfab")
    server.sendmail(sender, receiver, message)

