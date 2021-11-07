void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(1);
  pinMode(A0, INPUT);
  pinMode(A4, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  double photodiode = analogRead(A0);
  double pressureSens = analogRead(A4);
  double values[2] = {pressureSens, photodiode};
  if(Serial.availableForWrite() > 16){
    Serial.println(String(values[0]) + "|" + String(values[1]) + "|");
  }
}
