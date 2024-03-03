from flask import Flask 
import weather

app = Flask(__name__)

@app.route("/")
def hello_world():
    forecast = weather.getforecast('Oslo')
    html = '%s\n<p>Hello, World!</p>' % forecast
    return html
