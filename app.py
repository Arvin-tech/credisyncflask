from flask import Flask, render_template, request, jsonify
from flask_mail import Mail
from dotenv import load_dotenv
import os
import smtplib

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__, static_folder='assets', static_url_path='/static')

# Mail configuration
EMAIL_SERVER = os.getenv("MAIL_SERVER")
EMAIL_PORT = int(os.getenv("MAIL_PORT"))  
EMAIL_USE_TLS = bool(int(os.getenv("MAIL_USE_TLS")))
EMAIL_USERNAME = os.getenv("MAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
EMAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")

app.config.update(
    MAIL_SERVER=EMAIL_SERVER,
    MAIL_PORT=EMAIL_PORT,
    MAIL_USE_TLS=EMAIL_USE_TLS,
    MAIL_USERNAME=EMAIL_USERNAME,
    MAIL_PASSWORD=EMAIL_PASSWORD,
    MAIL_DEFAULT_SENDER=EMAIL_DEFAULT_SENDER,
)

mail = Mail(app)

@app.route('/send_approval_email', methods=['POST'])
def send_approval_email(recipient):
    subject = "Approval Notification"
    message = "Your request has been approved!"
    
    text = f"Subject: {subject}\n\n{message}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USERNAME, recipient, text)
    except Exception as e:
        raise e  

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/members')
def members():
    return render_template('members.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/evaluation')
def evaluation():
    return render_template('evaluation.html')

@app.route('/404')
def page_notfound():
    return render_template('notfound.html')

# @app.route('/send_approval_email', methods=['POST'])
# def send_approval_email_route():
#     recipient = request.json.get('recipient')
#     if recipient:
#         try:
#             send_approval_email(recipient)
#             return jsonify({"message": "Email sent successfully!"}), 200
#         except Exception as e:
#             return jsonify({"error": str(e)}), 500
#     return jsonify({"error": "Recipient not provided."}), 400

# Test route to send email without input
@app.route('/send_test_email', methods=['GET'])
def send_test_email():
    recipient = "dellogarciano@gmail.com"
    try:
        send_approval_email(recipient)
        return jsonify({"message": "Test email sent successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
