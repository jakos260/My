unsigned long t = 0;
int Fp = 5; //częstotliwość próbkowania
int T = 1000/Fp;

void setup()
{
  Serial.begin(9600);
  pinMode(10, INPUT);
  pinMode(11, INPUT);
}

void loop()
{
  t = millis();
  if (t%T == 0)
  {
    if((digitalRead(10) == 1)||(digitalRead(11) == 1))
    {
      Serial.println('!');
    }
    else
    {
      Serial.println(analogRead(A0));
      Serial.print(' ');
      Serial.print(t);
    }   
  }
}
