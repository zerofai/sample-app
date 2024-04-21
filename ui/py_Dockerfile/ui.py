from flask import Flask, render_template, jsonify
import os
import requests

template_dir = os.path.abspath('')  # Set the template directory to the current directory
CONTAINER_PORT = os.getenv('containerPort', '5000')  # Read containerPort from environmental variable
GREETING_HOSTNAME = os.getenv('GREETING_HOSTNAME', 'greeting')  # Read Greeting API hostname from environmental variable
WEATHER_HOSTNAME = os.getenv('WEATHER_HOSTNAME', 'weather')  # Read Weather API hostname from environmental variable
IMAGE_HOSTNAME = os.getenv('IMAGE_HOSTNAME', 'image')  # Read Image API URL from environmental variable
NAMEGEN_HOSTNAME = os.getenv('NAMEGEN_HOSTNAME', 'namegen')  # Read Image API URL from environmental variable

app = Flask(__name__, template_folder=template_dir)

service_na = {'error': 'Backend service not available'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greeting', methods=['GET'])
def get_greeting():
    greeting_api_url = f"http://{GREETING_HOSTNAME}/v1/greeting"
    try:
        greeting_response = requests.get(greeting_api_url)
        if greeting_response.status_code == 200:
            greeting_response.raise_for_status()  # Raise an exception for non-200 status codes
            greeting = greeting_response.json()
            return jsonify(greeting)
        else:
            return jsonify(service_na)
    except requests.exceptions.RequestException as e:
        return jsonify(service_na)

@app.route('/weather', methods=['GET'])
def get_weather():
    weather_api_url = f"http://{WEATHER_HOSTNAME}/v1/flw"
    try:
        weather_response = requests.get(weather_api_url)
        if weather_response.status_code == 200:
            weather_response.raise_for_status()  # Raise an exception for non-200 status codes
            weather = weather_response.json()
            return jsonify(weather)
        else:
            return jsonify(service_na)
    except requests.exceptions.RequestException:
        return jsonify(service_na)

@app.route('/image', methods=['GET'])
def get_image():
    image_api_url = f"http://{IMAGE_HOSTNAME}/v1/image"
    try:
        image_response = requests.get(image_api_url)
        if image_response.status_code == 200:
            image_response.raise_for_status()  # Raise an exception for non-200 status codes
            image = image_response.content
            return image
        else:
            return jsonify(service_na)
    except requests.exceptions.RequestException:
        return jsonify(service_na)

@app.route('/namegen', methods=['GET'])
def get_namegen():
    namegen_api_url = f"http://{NAMEGEN_HOSTNAME}/v1/name"
    try:
        namegen_response = requests.get(namegen_api_url)
        if namegen_response.status_code == 200:
            namegen_response.raise_for_status()  # Raise an exception for non-200 status codes
            namegen = namegen_response.text  # Get the response as a string
            return jsonify({"name": namegen})
        else:
            return jsonify(service_na)
    except requests.exceptions.RequestException as e:
        return jsonify(service_na)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def fallback(path):
    return jsonify(message="Sorry, please use the right endpoint")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=CONTAINER_PORT)