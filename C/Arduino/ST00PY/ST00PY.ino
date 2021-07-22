unsigned long t = 0;
unsigned long t_old = -1;
int Fp = 10; // częstotliwość próbkowania
int T = 1000/Fp;

void setup()
{
  Serial.begin(57600);
  pinMode(A2, INPUT);
}

void loop()
{
  t = millis(); // odczyt aktualnego czasu uc
  if (t%T == 0 && t != t_old) // jeśli t jest wielokrotnością okresu T
                              // i nie było jeszcze zbierane obywa się próbkowanie
  {
    Serial.print(t);
    Serial.print('x');
    Serial.println(analogRead(A2));
  }
  t_old = t;
}
