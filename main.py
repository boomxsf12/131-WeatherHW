from flask import Flask, jsonify
import requests
import pytest

# Step 1: Create a sample Weather Station application
app = Flask(__name__)


@app.route('/weather', methods=['GET'])
def get_weather_data():
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=London&appid=9af315419ae92983801fa2bd2cf88561')
    data = response.json()
    return jsonify(data)


# Step 2: Write tests for the Weather Station application
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_weather_data(client):
    rv = client.get('/weather')
    assert rv.status_code == 200


if __name__ == '__main__':
    app.run(debug=True)
# go to http://127.0.0.1:5000/weather in browser