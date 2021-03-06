#include <OneWire.h>
#include <DallasTemperature.h>
#include <time.h>
#include "Arduino.h"

#define ONE_WIRE_BUS 5; // czujnik temperatury D5, patrzeć na schemat -> R 1K2!!!
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
float t;

int l_sensor = A1; ///fotorezystor A1
int l;

void setup(void)
{
  
  Serial.begin(9600);
  sensors.begin();

}
 
void loop(void)
{
  
  sensors.requestTemperatures();
  t = sensors.getTempCByIndex(0);
  l = analogRead(l_sensor);
 
  Serial.print(t);
  Serial.print(" ");
  Serial.print(l);
  Serial.print("\n");
  
  
  delay(50);
}
