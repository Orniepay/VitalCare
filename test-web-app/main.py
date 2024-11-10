from flask import Flask, render_template_string # type: ignore
import serial                                   # type: ignore

app = Flask(__name__)
arduino = serial.Serial("COM6", 9600)

@app.route('/')
def index():
    return render_template_string('''
        <h1>arduino C LED Control</h1>
        <p><a href="/turn_on">Turn ON LED to red</a></p>
        <p><a href="/turn_off">Turn LED to green and show data</a></p>
    ''')

@app.route('/turn_on')
def turn_on():
    # arduino.write(b'a')  # Send 'a' to turn on the LED (red)
    return "<p>LED turned ON to red. <a href='/'>Go back</a></p>"

@app.route('/turn_off')
def turn_off():
    # arduino.write(b'b')  # Send 'b' to turn off the LED (green)
    return render_template_string('''
        <h1>LED turned OFF to green</h1>
        <p><a href="/">Go back</a></p>
        <p><span id="arduino-data">Waiting for data...</span></p>

        <script>
            function fetchArduinoData() {
                fetch('/get_arduino_data')
                    .then(response => response.text())
                    .then(data => {
                        document.getElementById('arduino-data').innerText = data;
                    })
                    .catch(error => console.error('Error:', error));
            }

            setInterval(fetchArduinoData, 2500);
        </script>
    ''')

@app.route('/get_arduino_data')
def get_arduino_data():
    if arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8').strip()
        print("BPM:", line)
        return line

if __name__ == '__main__':
    app.run(debug=True)
