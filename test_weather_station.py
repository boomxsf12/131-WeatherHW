import pytest
from weather_station import app
import sqlite3
import pandas as pd

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_submit_data(client):
    response = client.post('/submit', data=dict(temperature='25', humidity='50', pressure='1013'))
    assert b'Success' in response.data

    conn = sqlite3.connect('weather_data.db')
    df = pd.read_sql_query('SELECT * FROM weather', conn)
    conn.close()

    assert len(df) == 1
    assert df['temperature'][0] == 25.0
    assert df['humidity'][0] == 50.0
    assert df['pressure'][0] == 1013.0

def test_data_analysis(client):
    response = client.get('/data')
    assert b'Average Temperature' in response.data
