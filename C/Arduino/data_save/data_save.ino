#include <OneWire.h>
#include <DallasTemperature.h>
#include <time.h>

#define ONE_WIRE_BUS 5 // czujnik temperatury D5, patrzeć na schemat -> R 1K2!!!
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
float temp;

int l_sensor = A1; ///fotorezystor A5
int light;

void setup(void)
{
  
  Serial.begin(9600);
  sensors.begin();
  pinMode(2, OUTPUT);   /// LED D2
  
}
 
void loop(void)
{
  
  sensors.requestTemperatures();
  temp = sensors.getTempCByIndex(0);
  light = analogRead(l_sensor);
  //Serial.print("\nTEMP");
  Serial.print(temp); 
  Serial.print('x');
  Serial.println(light);
  
  if (temp > 23) digitalWrite (2, HIGH);
  else digitalWrite (2, LOW);
  
  //delay(100);
}
