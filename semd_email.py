import smtplib, ssl
import os


def email_sending(message):
    host = "smtp.gmail.com"
    port = 465
    username = "pan2kaj12@gmail.com"
    password = os.getenv("Portfolio_PASSWORD")
    receiver = "pan2kaj12@gmail.com"
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)





