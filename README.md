<div align="center">
  <h1 style="font-size: 50px">VitalCare</h1>
</div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="static/images/stethoscope.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">VitalCare: Remote Patient Monitoring System</h3>

  <p align="center">
    Concerned about your health? Let us help you with that!
  </p>
  <p align="center">
    Test your heartbeat, temperature, and alcohol level at our website to get the quickest and most accurate result.
  </p>
</div>
<br />

<!-- ABOUT THE PROJECT -->
## About The Project
![screenshot](https://github.com/user-attachments/assets/ae8a34df-2bbf-40b7-8907-b63d1e42dd37)

Not many users have the time or the convenience to go to the hospital to check if they have a serious medical condition, and some are clueless about how to check their health status. Luckily enough, VitalCare is here to help! With our newly developed in-built medical equipment from Arduino microcontroller, alcohol sensors, heartbeat monitor, and user-friendly website, our clients now can:

* Monitor their heartbeat on the website
* Check their alcohol condition directly on our in-built hardware
* Get a record of their previous health status

### Challenges we ran into
Connecting the sensor readings from Arduino into the framework Flask on Python.

### Accomplishments that we're proud of
The general UI of the project and the authentication system and being able to detect accurate readings on the sensors.

### What we learned
Connecting hardware with software is a lot more challenging than we thought. Generating the individual sensor readings turned out to be easier than we expected, but actually connecting the data from those sensors to a web application is a hard process that we are still figuring out.

### Built With
![Python](https://img.shields.io/badge/Python-black?style=for-the-badge&logo=python&logoColor=FFD43B)
![Docker](https://img.shields.io/badge/Docker-black?style=for-the-badge&logo=docker&logoColor=62D2FF)
![JavaScript](https://img.shields.io/badge/JavaScript-black?style=for-the-badge&logo=javascript&logoColor=FFFF00)
![HTML](https://img.shields.io/badge/HTML-black?style=for-the-badge&logo=html5&logoColor=FFA736)
![CSS](https://img.shields.io/badge/CSS-black?style=for-the-badge&logo=css3&logoColor=62D2FF)

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Running the Website
1. First, we clone the repository:
```
git clone https://github.com/Ornipay/ubh-fall2024.git
cd ubh-fall2024
```

2. Next, we cd into the folder that we have cloned
3. Finally, we type the following command in the terminal:

```
docker compose up --build --force-recreate
```

### Running the Sensors
1. Connect both the alcohol and the heart rate sensors to the Arduino
2. Afterwards, connect the Arduino to the computer 

## What's next?
* Adding a body temperature sensor to incorporate more vital checking to have more usability for the user.
* Integrate live sensor data into the website.
* Diagnose health conditions through Machine Learning and Pattern Recognition.
