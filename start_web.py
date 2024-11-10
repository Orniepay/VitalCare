import subprocess, webbrowser, requests, time, serial #type: ignore

def wait_for_site(url):
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("200 ok")
                break
        except Exception:
            pass
        time.sleep(1)

def wait_for_tiva_plugin(port, baud_rate):
    while True:
        try:
            serial.Serial(port, baud_rate)
            break
        except serial.SerialException:
            time.sleep(1)

def main():
    wait_for_tiva_plugin("COM3", 115200)
    subprocess.run(["docker", "compose", "down"])
    subprocess.Popen(["docker", "compose", "up", "--build"])
    wait_for_site("http://localhost:8080/")
    webbrowser.open("http://localhost:8080/")

main()