import subprocess

subprocess.Popen(["flask", "--app", "main", "run"])
import webbrowser

# Open localhost on port 8080
webbrowser.open("http://127.0.0.1:5000")