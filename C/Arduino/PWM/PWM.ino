unsigned long t = 0;
unsigned long t_old = -1;
int F = 10; //częstotliwość
int T = 1000/F;
int h_pwm = 2;
int l_pwm = 10;
int counter_h = h_pwm;
int counter_l = 0;


void setup()
{
  Serial.begin(57600);
  pinMode(13, OUTPUT);
  pinMode(A2, INPUT);

}

void loop()
{
  
  t = millis();  
  if (t%T == 0 && t != t_old)
  {
      if (counter_l < l_pwm)
    {
      counter_l += 1;
      if (counter_l == l_pwm)
      {
        counter_h = 0;
        digitalWrite(13, HIGH);
      }
    }
    else if (counter_h < h_pwm)
    {
      counter_h += 1;
      if (counter_h == h_pwm)
      {
        counter_l = 0;
        digitalWrite(13, LOW);
      }
    }

    Serial.print(t);
    Serial.print('x');    
    Serial.println(analogRead(A2));    
  }
  t_old = t;
}
