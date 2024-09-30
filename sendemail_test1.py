import smtplib

email = input("sender: ")
receiver = input("receiver")

subject = 'test'
message = 'test_message'

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, "16digitapppass")
server.sendmail(email, receiver, text)

print("Email has been sent to "+receiver)