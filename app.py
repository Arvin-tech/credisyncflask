from flask import Flask, render_template
from flask_mail import Mail
from email_api import email_blueprint  # Import the blueprint

app = Flask(__name__, static_folder='assets', static_url_path='/static')

# Register the email blueprint
app.register_blueprint(email_blueprint)

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

if __name__ == '__main__':
    app.run(debug=True)
