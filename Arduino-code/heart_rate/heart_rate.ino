void setup() {
  Serial.begin(9600); // sets the serial port to 9600
	Serial.println("MQ3 warming up!");
	//delay(20000); // allow the MQ3 to warm up
}

void loop()
{
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
    float BAC = 0.08 + (sensorValue - 400) * 0.0001;
    Serial.print("BAC: ");
    Serial.print(BAC, 3);
    Serial.println("%");
  }
}