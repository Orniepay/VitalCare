from flask import Flask, render_template_string
import serial

app = Flask(__name__)
arduino = serial.Serial("COM6", 9600)

@app.route('/')
def index():
    return render_template_string('''
            <h1>arduino C LED Control</h1>
            <p><a href="/turn_on">Turn ON LED to red</a></p>
            <p><a href="/turn_off">Turn LED to green</a></p>
            <script>
                function fetchArduinoData() {
                    fetch('/get_data')
                        .then(response => response.json())
                        .then(data => {
                            document.getElementById('arduino-data').innerText = data.message;
                        })
                        .catch(error => console.error('Error:', error));
                }
                setInterval(fetchArduinoData, 2500);
            </script>
        ''')

@app.route('/turn_on')
def turn_on():
    #arduino.write(b'a')  # Send '1' to arduino C to turn on the LED
    return "<p>LED turned ON to red. <a href='/'>Go back</a></p>"

#@app.route('/turn_off')
#def turn_off():
    #arduino.write(b'b')  # Send '0' to arduino C to turn off the LED
    #while arduino.in_waiting > 0:
        # Read the whole line
    #line = arduino.readline().decode('utf-8').rstrip()
#    line = arduino.readline().decode('utf-8').strip()
#    print("BPM:", line)
#    return f"{line}"

@app.route('/turn_off')
def turn_off():
    #arduino.write(b'b')  # Send '0' to arduino C to turn off the LED
    return "<p>LED turned OFF to green. <a href='/'>Go back</a></p>"

@app.route('/get_data')
def get_data():
    line = arduino.readline().decode('utf-8').strip()
    print("BPM:", line)
    return jsonify(message=line)
