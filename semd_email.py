import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "pan2kaj12@gmail.com"
password = "solv ggaq osih qbbo"

receiver = "pan2kaj12@gmail.com"
my_context = ssl.create_default_context()

message = """/
Hii !!
My name is pankaj
"""

with smtplib.SMTP_SSL(host, port, context=my_context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)




