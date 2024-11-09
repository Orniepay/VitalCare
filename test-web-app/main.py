from flask import Flask, jsonify
import serial

app = Flask(__name__)
arduino = serial.Serial("COM6", 9600)

@app.route('/')
def index():
    return '''<h1>arduino C LED Control</h1>
              <p><a href="/turn_on">Turn ON LED to red</a></p>
              <p><a href="/turn_off">Turn LED to green</a></p>'''

@app.route('/turn_on')
def turn_on():
    #arduino.write(b'a')  # Send '1' to arduino C to turn on the LED
    return "<p>LED turned ON to red. <a href='/'>Go back</a></p>"

@app.route('/turn_off')
def turn_off():
    #arduino.write(b'b')  # Send '0' to arduino C to turn off the LED
    #while arduino.in_waiting > 0:
        # Read the whole line
    line = arduino.readline().decode('utf-8').strip()  # Reads until newline
    print("Received:", line)
    #line = arduino.readline().decode('utf-8').rstrip()
    return jsonify(f"<p>{line} <a href='/'>Go back</a></p>")