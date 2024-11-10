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
    return render_template_string('''
        <h1>LED turned on to efwwe</h1>
        <p><a href="/">Go back</a></p>
        <p><span id="arduino-data1">Waiting for data...</span></p>

        <script>
            function fetchArduinoData() {
                fetch('/get_arduino_data1')
                    .then(response => response.text())
                    .then(data => {
                        if(data.startsWith("BAC: ")) document.getElementById('arduino-data1').innerText = "Waiting for data...";
                        else document.getElementById('arduino-data1').innerText = data;
                    })
                    .catch(error => console.error('Error:', error));
            }
            setInterval(fetchArduinoData, 2500);
        </script>
    ''')

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
                        if(data.startsWith("BPM: ")) document.getElementById('arduino-data').innerText = "Waiting for data...";
                        else document.getElementById('arduino-data').innerText = data;
                    })
                    .catch(error => console.error('Error:', error));
            }

            setInterval(fetchArduinoData, 2500);
        </script>
    ''')

@app.route('/get_arduino_data')
def get_arduino_data():
    arduino.write(b"a")
    if arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8').strip()
        #print("BPM:", line)
        return line

    
@app.route('/get_arduino_data1')
def get_arduino_data1():
    arduino.write(b"b")
    if arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8').strip()
       # print(line)
        return line
if __name__ == '__main__':
    app.run(debug=True)