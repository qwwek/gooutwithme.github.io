from flask import Flask, render_template, request
import weather

app = Flask(__name__)

@app.route("/")
def hello_world():
    forecast = weather.getforecast('Oslo')
    return render_template('index.html', data="123")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if len(email) == 0 or len(password) == 0:
            return render_template('error.html')
        
        return render_template('login.html')
    else:
        return render_template('login.html')
