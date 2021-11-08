int pin = 7;
void setup() {
  Serial.begin(115200);
  pinMode(pin, OUTPUT);
  digitalWrite(pin, LOW);
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
      digitalWrite(pin, HIGH);
    } else {
      digitalWrite(pin, LOW);
    }
  }
}
