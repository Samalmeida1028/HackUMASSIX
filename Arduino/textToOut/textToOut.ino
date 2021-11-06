void setup() {
    Serial.begin(9600); 
    Serial.println("Ready");
    pinMode(7, OUTPUT);
}

void loop() {
    char input_data[2];
    bool low_high;

    if(Serial.available() >= 2){
         for (int i=0; i<2; i++) {
             input_data[i] = Serial.read();
             Serial.println(input_data[i]);
         if (input_data[1] == 0){
          low_high = false;
         }
         else{
          low_high=true;
          Serial.println(input_data);
         } 
    }


        if(low_high) {
            digitalWrite(7,HIGH);
            delay(1000);
            digitalWrite(7,LOW);
            delay(1000);
        } else {
            digitalWrite(7,LOW);
            delay(1000);
            digitalWrite(7,HIGH);
            delay(1000);
        }
    } 
}
