# HackUMASSIX


__Organisers: Samuel, Tirth, Arjun and Chinguun__

In this project, we build a MORSE code detector that takes in light pulses, sound pulses, and written English characters as input and compares that to the MORSE database to output a message in English or flash an LED in MORSE. 

## Programming: 
We linked the Arduino IDE to PyCharm using the pyserial API. A simple .ino file was made to push into the Arduino Uno board which contained the startup instructions. This code is uploaded into the board. 

In the Python IDE, we use the [pyserial API](https://pyserial.readthedocs.io/en/latest/pyserial_api.html) to create an object reference to the Arduino board. Then, we can read the Serial line. This line will output a string with two values in it separated by a "|". The first value is the voltage from the [photoresistor)](https://arduinomodules.info/ky-018-photoresistor-module/) (PD) and the second value is the value from a [force sensitive resistor](https://learn.adafruit.com/force-sensitive-resistor-fsr) (PS). 

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



## Morse Code

After this, it was time to actually create the logic. We first created a dictionary that stored pairs of values to look in, and had each character used in english and its corresponding morse code translation.

```
        self.text = {'A': '.-', 'B': '-...',
                           'C': '-.-.', 'D': '-..', 'E': '.',
                           'F': '..-.', 'G': '--.', 'H': '....',
                           'I': '..', 'J': '.---', 'K': '-.-',
                           'L': '.-..', 'M': '--', 'N': '-.',
                           'O': '---', 'P': '.--.', 'Q': '--.-',
                           'R': '.-.', 'S': '...', 'T': '-',
                           'U': '..-', 'V': '...-', 'W': '.--',
                           'X': '-..-', 'Y': '-.--', 'Z': '--..',
                           '1': '.----', '2': '..---', '3': '...--',
                           '4': '....-', '5': '.....', '6': '-....',
                           '7': '--...', '8': '---..', '9': '----.',
                           '0': '-----', ',': '--..--', '.': '.-.-.-',
                           '?': '..--..', '/': '-..-.', '-': '-....-',
                           '(': '-.--.', ')': '-.--.-', ' ':'   '}
  ```
  
  This was the easy part. The harder part ws converting to morse code back into english as we had to account for some elements being the prefixes for others. For example, E in morse code is just '.' but that is also the start of 'L', 'P', 'S' etc. So we had to take this into consideration when we solved it. Our solution was to append spaces to the end for every character, as in morse code they denote a change of character by 3 *"dits"* which is the short signal.
