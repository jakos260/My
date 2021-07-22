int dataPin = 8;
int latchPin = 9;
int clockPin = 10;
int mq3_analogPin = A0;
int a;

int numOfRegisters = 2;
byte* registerState;

long effectId = 0;
long prevEffect = 0;
long effectRepeat = 0;
long effectSpeed = 30;

void setup()
{
  Serial.begin(9600);
  
  registerState = new byte[numOfRegisters];
  for (size_t i = 0; i < numOfRegisters; i++)
  {
    registerState[i] = 0;
  }

  pinMode(latchPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);

}

void loop()
{
  int mq3_value = analogRead(mq3_analogPin);
  int a = ((mq3_value)*0.084);
  Serial.println(mq3_value);

  delay(100);

}
