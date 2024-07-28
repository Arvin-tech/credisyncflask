from flask import Flask, render_template

app = Flask(__name__, static_folder='assets', static_url_path='/static')

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/members')
def members():
    return render_template('members.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True)
