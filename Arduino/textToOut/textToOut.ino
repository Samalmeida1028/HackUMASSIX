#include "SerialTransfer.h"

SerialTransfer myTransfer;

void setup() {
  Serial.begin(115200);
  myTransfer.begin(Serial);
  pinMode(7, OUTPUT);
}

void loop() {
  digitalWrite(7, HIGH);
  for (uint16_t i = 0; i < 200; i++) {
    myTransfer.packet.txBuff[i] = myTransfer.packet.rxBuff[i];
  }

  myTransfer.sendData(myTransfer.bytesRead);

  int input_data[2];
  input_data[0] = myTransfer.packet.txBuff[0];
  input_data[1] = myTransfer.packet.txBuff[1];

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
  delay(input_data[0] * 1000);
}
