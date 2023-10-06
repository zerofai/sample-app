from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/v1/flw', methods=['GET'])
def get_weather():
    weather_api_url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=en'
    response = requests.get(weather_api_url)
    weather = response.json()
    return jsonify(weather)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def fallback(path):
    return jsonify(message="Sorry, please use the right endpoint")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
