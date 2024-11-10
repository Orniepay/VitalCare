int BPM = 0;
float sensorValue;
void setup() {
  Serial.begin(9600); // sets the serial port to 9600
	Serial.println("MQ3 warming up!");
	//delay(20000); // allow the MQ3 to warm up
}
int RS = 48; //Alcohol sensor value in clear air.
int RO = 585; //Alchol sensor value in clear air (average).
void loop()
{
  sensorValue = analogRead(A0); // read analog input pin 0

	if(sensorValue < 120) Serial.println("BAC: 0.000%");
  else if(sensorValue > 120 && sensorValue < 400)
  {
    float BAC = ((sensorValue - 120) / 280) * 0.08;
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

  delay(2000);
	// delay(2000); // wait 2s for next reading
  // analogWrite(A0, 120);
  // int sensorValue = analogRead(A0);
  // //calculate_BPM(sensorValue);
  // Serial.println(sensorValue);
  // delay(2500);

}

void calculate_BPM(int sensor_value)
{
  BPM = map(sensor_value, 0, 1023, 0, 150);
  if(BPM <= 30) Serial.println("BPM: 0");
  else if(BPM <= 150)
  {
      if(BPM >= 120) Serial.print("Move your fingers back a bit. ");
      if(BPM >= 30 && BPM <= 45) Serial.print("Move your fingers forward a bit. ");
      Serial.print("BPM: ");
      Serial.println(BPM);
  }
}