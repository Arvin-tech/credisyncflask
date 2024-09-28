# import sa email api
from flask_mail import Mail, Message
from flask import Flask, Blueprint, request, jsonify

#get the variables from .env file
from dotenv import load_dotenv
import os

#load them in this file
load_dotenv()

# Create a Blueprint
email_blueprint = Blueprint('email_api', __name__)

# declare og variables para sa email api (values from env)
EMAIL_SERVER_NI_SHA = os.getenv("MAIL_SERVER")
EMAIL_PORT_NI_SHA = os.getenv("MAIL_PORT")
EMAIL_USE_TLS_NI = os.getenv("MAIL_USE_TLS")
EMAIL_USERNAME = os.getenv("MAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
EMAIL_SENDER_CREDISYNC = os.getenv("MAIL_DEFAULT_SENDER")

app = Flask(__name__) 

# Mail configuration
app.config['MAIL_SERVER'] = EMAIL_SERVER_NI_SHA
app.config['MAIL_PORT'] = EMAIL_PORT_NI_SHA
app.config['MAIL_USE_TLS'] = EMAIL_USE_TLS_NI
app.config['MAIL_USERNAME'] = EMAIL_USERNAME
app.config['MAIL_PASSWORD'] = EMAIL_PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = EMAIL_SENDER_CREDISYNC

mail = Mail(app)

def send_approval_email(recipient):
    subject = "Approval Notification"
    body = "Your request has been approved!"
    
    msg = Message(subject, recipients=[recipient])
    msg.body = body
    mail.send(msg)

@email_blueprint.route('/send_approval_email', methods=['POST'])
def send_approval_email_route():
    recipient = request.json.get('recipient')
    if recipient:
        try:
            send_approval_email(recipient)
            return jsonify({"message": "Email sent successfully!"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"error": "Recipient not provided."}), 400
