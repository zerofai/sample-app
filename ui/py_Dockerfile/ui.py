from flask import Flask, render_template, jsonify
import os
import requests

template_dir = os.path.abspath('')  # Set the template directory to the current directory
GREETING_HOSTNAME = os.getenv('GREETING_HOSTNAME')  # Read Greeting API hostname from environmental variable
WEATHER_HOSTNAME = os.getenv('WEATHER_HOSTNAME')  # Read Weather API hostname from environmental variable

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greeting', methods=['GET'])
def get_greeting():
    greeting_api_url = f"http://{GREETING_HOSTNAME}/v1/greeting"
    greeting_response = requests.get(greeting_api_url)
    greeting_response.raise_for_status()  # Raise an exception for non-200 status codes
    greeting = greeting_response.json()
    return greeting

@app.route('/weather', methods=['GET'])
def get_weather():
    weather_api_url = f"http://{WEATHER_HOSTNAME}/v1/flw"
    weather_response = requests.get(weather_api_url)
    weather_response.raise_for_status()  # Raise an exception for non-200 status codes
    weather = weather_response.json()
    return weather

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def fallback(path):
    return jsonify(message="Sorry, please use the right endpoint")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
