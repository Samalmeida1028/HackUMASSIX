void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(1);
  pinMode(A0, OUTPUT);
  pinMode(A1, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  double photodiode = analogRead(A0);
  double pressureSens = analogRead(A1);
  double values[2] = {photodiode, pressureSens};
  Serial.print(String(values[1]) + "|" + String(values[2]) + "|");
  Serial.println();
}
