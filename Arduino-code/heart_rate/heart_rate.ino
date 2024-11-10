int BPM = 0;
void setup() {
  Serial.begin(9600);
}

void loop()
{
  int sensorValue = analogRead(A0);
  BPM = map(sensorValue, 0, 1023, 0, 150);
  if(BPM <= 30) Serial.println("BPM: 0");
  else if(BPM <= 150)
  {
      if(BPM >= 120) Serial.print("Move your fingers back a bit. ");
      if(BPM >= 30 && BPM <= 45) Serial.print("Move your fingers forward a bit. ");
      Serial.print("BPM: ");
      Serial.println(BPM);
  }
  
  delay(2500);
}