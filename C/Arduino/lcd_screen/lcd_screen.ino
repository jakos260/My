
#include <LiquidCrystal.h>
LiquidCrystal lcd (12, 11, 5, 4, 3, 2);

void setup() {
  
lcd.begin (16, 2);
lcd.print ("cos");


int q = digitalRead(7);
 int w = digitalRead(8);
 int e = digitalRead(9);

pinMode(7,INPUT);
pinMode(8,INPUT);
pinMode(9,INPUT);
}

void loop() {

  int q = digitalRead(7);
  lcd.setCursor (2,2);
  lcd.print ( q );
  delay(25);

  int w = digitalRead(8);
  lcd.setCursor (6,2);
  lcd.print ( w );
  delay(25);

  int e = digitalRead(9);
  lcd.setCursor (10,2);
  lcd.print ( e );
  delay(25);
  
  

}
