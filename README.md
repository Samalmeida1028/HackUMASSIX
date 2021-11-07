# HackUMASSIX


<h>PROJECT<h>
Organisers: Samuel, Tirth, Arjun and Chinguun

In this project, we build a MORSE code detector that takes in light pulses, sound pulses, and written English characters as input and compares that to the MORSE database to output a message in English or flash an LED in MORSE. 

Programming: 
We linked the Arduino IDE to PyCharm using the pyserial API. A simple .ino file was made to push into the Arduino Uno board which contained the startup instructions. This code is uploaded into the board. 

In the Python IDE, we use the pyserial API to create an object reference to the Arduino board. Then, we can read the Serial line. This line will output a string with two values in it separated by a "|". The first value is the voltage from the photodiode (PD) and the second value is the value from the pressure sensor (PS). 

The code snipped below shows the Arduino startup code. 
```
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);
  pinMode(A0, OUTPUT);
  pinMode(A1,OUTPUT);
}

void loop() {
  double photodiode = analogRead(A0);
  double pressureSens = analogRead(A1);
  Serial.println(String(photodiode) + " | " + String(pressureSens));
}
```

We then compare these output voltages to a threshold voltage for each component. Below is the pseudocode for comparing to thresholds. Notice that this form will covert the analog values into digital binary values to signify ON or OFF. 
```
if read_value >= threshold_value:
  output 1
else:
  output 0
```

Since the PD has more sensitivity than the PS, it will have a higher offset voltage to begin with depending on how well lit the environment is. So the threshold value of the PD will be higher than that of the PS, since the PS starts from 0 as no force is applied to begin with. 
