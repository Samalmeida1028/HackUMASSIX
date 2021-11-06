void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(1);
  Serial.println("Arduino is ready!");
  pinMode(A0, OUTPUT);
  pinMode(A1, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  double photodiode = analogRead(A0);
  double pressureSens = analogRead(A4);
  double values[2] = {pressureSens, photodiode};
  Serial.print(String(values[0]) + "|" + String(values[1]) + "|");
  Serial.println();
}
