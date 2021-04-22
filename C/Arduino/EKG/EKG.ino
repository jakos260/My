/******************************************************************************
Heart_Rate_Display.ino
Demo Program for AD8232 Heart Rate sensor.
Casey Kuhns @ SparkFun Electronics
6/27/2014
https://github.com/sparkfun/AD8232_Heart_Rate_Monitor
The AD8232 Heart Rate sensor is a low cost EKG/ECG sensor.  This example shows
how to create an ECG with real time display.  The display is using Processing.
This sketch is based heavily on the Graphing Tutorial provided in the Arduino
IDE. http://www.arduino.cc/en/Tutorial/Graph
Resources:
This program requires a Processing sketch to view the data in real time.
Development environment specifics:
  IDE: Arduino 1.0.5
  Hardware Platform: Arduino Pro 3.3V/8MHz
  AD8232 Heart Monitor Version: 1.0
This code is beerware. If you see me (or any other SparkFun employee) at the
local pub, and you've found our code helpful, please buy us a round!
Distributed as-is; no warranty is given.
******************************************************************************/

void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(10, INPUT);
  pinMode(11, INPUT);
}

void loop()
{
  digitalWrite(13, HIGH);
  if((digitalRead(10) == 1)||(digitalRead(11) == 1))
  {
    Serial.println('!');
  }
  else
  {
    
//      Serial.print('0');
//      Serial.print(' ');
      Serial.println(analogRead(A0));

//      delay(5);
  }

  digitalWrite(13, LOW);
}
