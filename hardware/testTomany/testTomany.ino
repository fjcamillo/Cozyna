int detector1 = 52;
int detector2 = 53;
int detector3 = 50;
int detector4 = 51;
int detector5 = 48;
int detector6 = 49;
int detector7 = 46;
int detector8 = 47;
int detector9 = 44;
int detector10 = 45;


int sense1 = A0;
int sense2 = A1;
int sense3 = A2;
int sense4 = A3;
int sense5 = A4;
int sense6 = A5;
int sense7 = A6;
int sense8 = A7;
int sense9 = A8;
int sense10 = A9;

int ldr1 = A10;
int ldr2 = A11;
int ldr3 = A12;
int ldr4 = A13;
int ldr5 = A14;
int ldr6 = A15;

int ldr1Value = 0;
int ldr2Value = 0;
int ldr3Value = 0;
int ldr4Value = 0;
int ldr5Value = 0;
int ldr6Value = 0;

String sit = "sit";
String entered = "entered";

int holder = 0;


void setup()
{
pinMode(detector1,OUTPUT);
pinMode(detector2,OUTPUT);
pinMode(detector3,OUTPUT);
pinMode(detector4,OUTPUT);
pinMode(detector5,OUTPUT);
pinMode(detector6,OUTPUT);
pinMode(detector7,OUTPUT);
pinMode(detector8,OUTPUT);
pinMode(detector9,OUTPUT);
pinMode(detector10,OUTPUT);
Serial.begin(9600);
}

void loop(){
  if (analogRead(sense1)) {
//    Serial.println("1");/
     holder = analogRead(sense1);
    Serial.println("sit sit "+ holder);
//    Serial.println("---");/
    delay(100);
  }
  if (analogRead(sense2)) {
//    Serial.println("2");/
holder = analogRead(sense2);
    Serial.println("sit sit "+ holder);
//    Serial.println("---");/
    delay(100);
  }
  if (analogRead(sense3)) {
//    Serial.println("3");/
holder = analogRead(sense3);
    Serial.println("sit sit "+ holder);
//    Serial.println("---");/
    delay(100);
  }
  if (analogRead(sense4)) {
//    Serial.println("4");/
holder = analogRead(sense4);
    Serial.println("sit sit "+ holder);
//    Serial.println("---");/
    delay(100);
  }
  if (analogRead(sense5)) {
//    Serial.println("5");/
holder = analogRead(sense5);
    Serial.println("sit sit "+ holder);
//    Serial.println("---");/
    delay(100);
  }
  if (analogRead(sense6)) {
//    Serial.println("6");/
holder = analogRead(sense6);
    Serial.println("sit sit "+ holder);
//    Serial.println("---");/
    delay(100);
  }
  if (analogRead(sense7)) {
//    Serial.println("7");/
holder = analogRead(sense7);
    Serial.println("sit sit "+ holder);
//    Serial.println("---");/
    delay(100);
  }
  if (analogRead(sense8)) {
//    Serial.println("8");/
holder = analogRead(sense8);
    Serial.println("sit sit "+ holder);
//    Serial.println("---");/
    delay(100);
  }
  if (analogRead(sense9)) {
//    Serial.println("9");/
holder = analogRead(sense9);
    Serial.println("sit sit "+ holder);
//    Serial.println("---");/
    delay(100);
  }
  if (analogRead(sense10)) {
//    Serial.println("10");/
holder = analogRead(sense10);
    Serial.println("sit sit "+holder);
//    Serial.println("---");/
    delay(100);
  }

  if (analogRead(ldr1)) {
//    Serial.println("11");/
  }
  if (analogRead(ldr2)) {
//    Serial.println("12");/
  }
  if (analogRead(ldr3)) {
//    Serial.println("13");/
  }
  if (analogRead(ldr4)) {
//    Serial.println("14");/
  }
  if (analogRead(ldr5)) {
//    Serial.println("15");/
  }
  if (analogRead(ldr6)) {
//    Serial.println("16");/
  }
  
}

void test()
{
  int val1 = analogRead(sense1);
  delay(500);
  int val2 = analogRead(sense2);
  delay(500);
  int val3 = analogRead(sense3);
  delay(500);
  int val4 = analogRead(sense4);
  delay(500);
  int val5 = analogRead(sense5);
  delay(500);
  int val6 = analogRead(sense6);
  delay(500);
  int val7 = analogRead(sense7);
  delay(500);
  int val8 = analogRead(sense8);
  delay(500);
  int val9 = analogRead(sense9);
  delay(500);
  int val10 = analogRead(sense10);
  delay(500);
//  String data = "IR1 " + val1;

  ldr1Value = analogRead(ldr1);
  delay(500);
  ldr2Value = analogRead(ldr2);
  delay(500);
  ldr3Value = analogRead(ldr3);
  delay(500);
  ldr4Value = analogRead(ldr4);
  delay(500);
  ldr5Value = analogRead(ldr5);
  delay(500);
  ldr6Value = analogRead(ldr6);
  delay(500);
  


  if (val1)
  {Serial.println("IR1: ");
  delay(100);}
//
//  if (val2)
//  {Serial.println("IR2 "+val2);
//  delay(100);}
//
//  if (val3)
//  {Serial.println("IR3 "+val3);
//  delay(100);}
//
//  if (val4)
//  {Serial.println("IR4 "+val4);
//  delay(100);}
//
//  if (val5)
//  {Serial.println("IR5 "+val5);
//  delay(100);}
//
//  if (val6)
//  {Serial.println("IR6 "+val6);
//  delay(100);}
//
//  if (val7)
//  {Serial.println("IR7 "+val7);
//  delay(100);}
//
//  if (val8)
//  {Serial.println("IR8 "+val8);
//  delay(100);}
//
//  if (val9)
//  {Serial.println("IR9 "+val9);
//  delay(100);}
//
//  if (val10)
//  {Serial.println("IR10 "+val10);
//  delay(100);}
//  

  if (ldr1Value)
  {Serial.println("LDR1: " + ldr1Value);
  delay(100);}
  
//  if (ldr2Value)
// {Serial.println("LDR2: " + ldr2Value);
//  delay(100);}
  
//  if (ldr3Value)
//  {Serial.println("LDR3: " + ldr3Value);
//  delay(100);}
  
//  if (ldr4Value)
//  {Serial.println("LDR4: " + ldr4Value);
//  delay(100);}
  
//  if (ldr5Value)
//  {Serial.println("LDR5: " + ldr5Value);
//  delay(100);}

//  if (ldr6Value)
//  {Serial.println("LDR6: " + ldr7Value);
//  delay(100);}

}
