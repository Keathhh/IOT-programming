from flask import Flask, render_template
import mysql.connector
import serial

app = Flask(__name__)

pins = {
    11: {'name': 'Green LED', 'state': 0},
    12: {'name': 'Red LED', 'state': 0},
    'A0': {'name': 'Smoke Sensor', 'state': 0},
    10: {'name': 'Buzzer', 'state': 0}
}

db_conn = mysql.connector.connect(host='localhost', user='root', password='cutie123', database='fire_db')
cursor = db_conn.cursor()

@app.route('/')
def index():
    # Fetch fire logs from the database
    cursor.execute("SELECT * FROM fire_logs")
    fire_logs = cursor.fetchall()
    
    # Prepare HTML to display fire logs
    fire_logs_html = "<h1>Fire Logs</h1>"
    fire_logs_html += "<ul>"
    for log in fire_logs:
        fire_logs_html += f"<li>{log[1]}</li>"  # Assuming 'fire_detected' is the second column
    fire_logs_html += "</ul>"

    templateData = {
        'pins': pins,
        'fire_logs': fire_logs_html
    }
    return render_template('index.html', **templateData)

@app.route("/<changePin>/<toggle>")
def toggle_function(changePin, toggle):
    changePin = int(changePin)
    deviceName = pins[changePin]['name']
    ser = serial.Serial('/dev/cu.usbmodem101', 9600, timeout=1)
    ser.flush()

    if toggle == "on":
        ser.write(str(changePin).encode())
        pins[changePin]['state'] = 1
        message = "Turned " + deviceName + " on."
    elif toggle == "off":
        ser.write(str(changePin + 10).encode())
        pins[changePin]['state'] = 0
        message = "Turned " + deviceName + " off."

    templateData = {
        'pins': pins
    }
    return render_template('index.html', **templateData)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
