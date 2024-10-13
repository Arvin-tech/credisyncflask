# import smtplib

# email = input("sender: ")
# receiver = input("receiver: ")

# subject = 'test'
# message = 'test_message'

# text = f"Subject: {subject}\n\n{message}"

# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()

# server.login(email, "oeerirbyssbuhhif")
# server.sendmail(email, receiver, text)

# print("Email has been sent to "+receiver)
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Input sender and receiver email addresses
email = input("Sender: ")
receiver = input("Receiver: ")

# Email subject
subject = 'Credisync - Loan Application Approved'

# Get the path to the email.html file
html_file_path = os.path.join('templates', 'email.html')

# Read the HTML content
with open(html_file_path, 'r') as file:
    html_content = file.read()

# Create the email
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = receiver
msg['Subject'] = subject

# Attach the HTML content to the email
msg.attach(MIMEText(html_content, 'html'))

# Setup the SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# Login to the email account
server.login(email, "oeerirbyssbuhhif")

# Send the email
server.sendmail(email, receiver, msg.as_string())

# Close the server
server.quit()

print("Email has been sent to " + receiver)

