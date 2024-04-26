from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    temperature = request.form['temperature']
    humidity = request.form['humidity']
    pressure = request.form['pressure']

    # Store data in SQLite database
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS weather (temperature REAL, humidity REAL, pressure REAL)')
    c.execute('INSERT INTO weather (temperature, humidity, pressure) VALUES (?, ?, ?)', (temperature, humidity, pressure))
    conn.commit()
    conn.close()

    return render_template('success.html')

@app.route('/data')
def data():
    # Retrieve data from SQLite database
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('SELECT temperature FROM weather')
    temperatures = c.fetchall()
    conn.close()

    # Calculate average temperature
    if temperatures:
        total_temperature = sum(temp[0] for temp in temperatures)
        avg_temperature = total_temperature / len(temperatures)
    else:
        avg_temperature = None

    return render_template('data.html', avg_temperature=avg_temperature)

if __name__ == '__main__':
    app.run(debug=True)
