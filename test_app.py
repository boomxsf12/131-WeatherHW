import pytest
from app import app  # Import the app object from app.py

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_weather_data(client):
    rv = client.get('/weather')
    assert rv.status_code == 200