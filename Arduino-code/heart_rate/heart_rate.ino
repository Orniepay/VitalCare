int pwmPin = 2; // PWM-capable pin for output
float minTemp = 0.0;   // Minimum temperature range of the sensor
float maxTemp = 100.0; // Maximum temperature range of the sensor

void setup() {
  Serial.begin(9600);
  pinMode(pwmPin, INPUT);
	//Serial.println("MQ3 warming up!");
	//delay(20000); // allow the MQ3 to warm up
}

void loop()
{
  int sensor_value = analogRead(A0); // read analog input pin 0
  calculate_BPM(sensor_value);
  calculate_BAC(sensor_value);
  calculate_temperature(sensor_value);
  int sensor_value = analogRead(A0); // read analog input pin 0
  if(Serial.available() > 0)
  {
    byte incoming = Serial.read();
    if(incoming == "a") calculate_BAC(sensor_value);
    else if(incoming == "b") calculate_BPM(sensor_value);
  }
  
  delay(2500);
}

void calculate_BPM(int sensor_value)
{
  int BPM = map(sensor_value, 0, 1023, 0, 150);
  if(BPM <= 30) Serial.println("BPM: 0");
  else if(BPM <= 150)
  {
      if(BPM >= 120) Serial.print("Move your fingers back a bit. ");
      if(BPM >= 30 && BPM <= 45) Serial.print("Move your fingers forward a bit. ");
      Serial.print("BPM: ");
      Serial.println(BPM);
  }
}

void calculate_BAC(int sensor_value)
{
  if(sensor_value < 120) Serial.println("BAC: 0.000%");
  else if(sensor_value > 120 && sensor_value < 400)
  {
    float BAC = ((sensor_value - 120) / 280) * 0.08;
    Serial.print("BAC: ");
    Serial.print(BAC, 3);
    Serial.println("%");
  }
  else
  {
    float BAC = 0.08 + (sensor_value - 400) * 0.0001;
    Serial.print("BAC: ");
    Serial.print(BAC, 3);
    Serial.println("%");
  }
}

void calculate_temperature(int temperature)
{
  Serial.print("Value: ");
  Serial.println(temperature);
  
  // if (temperature < minTemp) temperature = minTemp;
  // if (temperature > maxTemp) temperature = maxTemp;

  // // Map the temperature to PWM value (0-255)
  // int pwm_value = map(temperature, minTemp, maxTemp, 0, 255);

  // Serial.print("PWM Value: ");
  // Serial.println(pwm_value);
}