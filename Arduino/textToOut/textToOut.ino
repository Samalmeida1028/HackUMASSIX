void setup() {
  Serial.begin(115200);
  pinMode(7, OUTPUT);
  digitalWrite(7, LOW);
}

void loop() {
  if (Serial.available()) {
    String input_data = Serial.readString();

    Serial.println(input_data);
    bool on = false;
    
    if (input_data == "3" || input_data == "7") {
      on = true;
    }

    if (on) {
      digitalWrite(7, HIGH);
    } else {
      digitalWrite(7, LOW);
    }
  }
}
