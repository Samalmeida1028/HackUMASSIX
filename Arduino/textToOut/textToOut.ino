void setup() {
  Serial.begin(115200);
  pinMode(7, OUTPUT);
  digitalWrite(7, LOW);
}

void loop() {
  if (Serial.available()) {
    String input_data = Serial.readString();
    int stall;

    Serial.println(input_data);
    bool on = false;

    if (input_data == "2" || input_data == "3") {
      stall = 2;
    } else {
      stall = 6;
    }
    
    if (input_data == "3" || input_data == "7") {
      on = true;
    }

    if (on) {
      digitalWrite(7, HIGH);
    } else {
      digitalWrite(7, LOW);
    }
    delay(stall * 250);
  }
}
