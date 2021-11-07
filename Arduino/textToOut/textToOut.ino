void setup() {
  Serial.begin(115200);
  pinMode(7, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    String input_data = Serial.readString();
    int data[2];

    for (int i = 0; i < input_data.length(); i++) {
      data[i] = input_data[i];
    }
    Serial.println(input_data);
    bool low_high;

    if (input_data[1] == 0) {
      low_high = false;
    } else {
      low_high = true;
    }

    if (low_high) {
      digitalWrite(7, HIGH);
    } else {
      digitalWrite(7, LOW);
    }
  }
}
