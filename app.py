# app.py
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather_data():
    # Replace 'your_api_key' with your actual OpenWeatherMap API key
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=London&appid=0ea1e7a2709146d42f2260f90020d5bb')
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
