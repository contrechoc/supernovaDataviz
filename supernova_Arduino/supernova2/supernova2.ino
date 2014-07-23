
int arrayLength = 206;
int timeDelayTotal = 0;

char superNova[] = 
{

  3, 1, 
  4, 1, 
  0, 2, 
  3, 2, 
  3, 2, 
  4, 2, 
  3, 1, 
  4, 1, 
  3, 2, 
  4, 2, 
  0, 4, 
  2, 3, 
  4, 3, 
  0, 5, 
  4, 5, 
  2, 2, 
  4, 2, 
  2, 3, 
  2, 3, 
  2, 3, 
  3, 7, 
  4, 7, 
  4, 10, 
  2, 11, 
  2, 14, 
  4, 14, 
  1, 20, 
  2, 21, 
  2, 22, 
  3, 24, 
  0, 25, 
  3, 26, 
  4, 26, 
  2, 18, 
  3, 28, 
  4, 28, 
  2, 24, 
  2, 29, 
  2, 28, 
  3, 28, 
  4, 28, 
  2, 27, 
  4, 27, 
  2, 25, 
  4, 25, 
  4, 47, 
  1, 33, 
  2, 39, 
  4, 39, 
  2, 39, 
  4, 39, 
  2, 40, 
  4, 40, 
  2, 40, 
  4, 40, 
  2, 41, 
  2, 46, 
  2, 50, 
  4, 50, 
  2, 52, 
  2, 52, 
  2, 56, 
  3, 56, 
  4, 56, 
  0, 56, 
  2, 59, 
  4, 75, 
  2, 61, 
  3, 61, 
  4, 61, 
  1, 65, 
  2, 66, 
  3, 66, 
  4, 66, 
  2, 67, 
  3, 68, 
  3, 68, 
  3, 69, 
  3, 71, 
  4, 71, 
  3, 71, 
  4, 71, 
  2, 78, 
  4, 78, 
  2, 78, 
  4, 78, 
  2, 73, 
  4, 73, 
  2, 79, 
  4, 79, 
  2, 82, 
  4, 82, 
  2, 81, 
  4, 81, 
  2, 82, 
  4, 82, 
  2, 82, 
  4, 82, 
  2, 82, 
  4, 82, 
  2, 83, 
  2, 77, 
  2, 84, 
  3, 84, 
  4, 84, 
  2, 85, 
  4, 85, 
  3, 85, 
  3, 86, 
  3, 87, 
  4, 106, 
  2, 96, 
  2, 93, 
  4, 93, 
  3, 99, 
  3, 101, 
  4, 107, 
  2, 108, 
  3, 108, 
  2, 109, 
  4, 109, 
  3, 110, 
  2, 113, 
  4, 113, 
  2, 114, 
  3, 114, 
  4, 114, 
  4, 115, 
  4, 119, 
  3, 119, 
  4, 136, 
  3, 121, 
  2, 122, 
  4, 122, 
  3, 124, 
  2, 123, 
  0, 126, 
  1, 127, 
  3, 126, 
  2, 127, 
  3, 127, 
  2, 128, 
  2, 129, 
  3, 129, 
  1, 130, 
  2, 133, 
  3, 133, 
  1, 135, 
  0, 130, 
  2, 140, 
  3, 140, 
  4, 140, 
  2, 139, 
  4, 139, 
  3, 141, 
  3, 141, 
  3, 142, 
  4, 142, 
  2, 142, 
  3, 142, 
  4, 142, 
  3, 142, 
  3, 142, 
  3, 143, 
  2, 145, 
  3, 145, 
  4, 145, 
  3, 146, 
  2, 141, 
  0, 147, 
  2, 146, 
  2, 150, 
  4, 150, 
  3, 150, 
  2, 151, 
  4, 151, 
  0, 151, 
  2, 151, 
  3, 151, 
  4, 167, 
  4, 152, 
  1, 154, 
  3, 152, 
  2, 156, 
  3, 156, 
  2, 157, 
  2, 157, 
  2, 157, 
  0, 159, 
  3, 161, 
  0, 168, 
  2, 169, 
  0, 169, 
  3, 168, 
  4, 168, 
  1, 172, 
  1, 171, 
  2, 173, 
  3, 173, 
  4, 173, 
  1, 173, 
  1, 173, 
  1, 174, 
  2, 174, 
  0, 178, 
  0, 178, 
};

void setup(){
  for (int i=5; i<10; i++)
  {
    pinMode(i, OUTPUT);
    digitalWrite(i, HIGH);
    delay(2000);
  }
  delay(1000);
  for (int i=5; i<10; i++)
  {
    digitalWrite(i, LOW);
  }
  Serial.begin(9600);
}

void loop(){

  timeDelayTotal = 0;
  for ( int i=0; i< arrayLength; i+=2){

    int zone = superNova[i];
    int timeD = superNova[i+1];
    int pinNum = 0;
    if (zone == 0 ) pinNum = 6;
    if (zone == 1 ) pinNum = 5;
    if (zone == 2 ) pinNum = 8;
    if (zone == 3 ) pinNum = 7;
    if (zone == 4 ) pinNum = 9;

    Serial.print(i);
    Serial.print(" ");
    Serial.print(zone);
    Serial.print(" ");
    Serial.println(timeD);

    if ( timeD < timeDelayTotal ) timeD = timeDelayTotal;

    //on this garment we only have three led pannels

    digitalWrite( 9, HIGH);
    delay(50);
    digitalWrite( 8, HIGH);
    delay(50);
    digitalWrite( 7, HIGH);
    delay(50);

    digitalWrite( 9, LOW);
    delay(50);
    digitalWrite( 8, LOW);
    delay(50);
    digitalWrite( 7, LOW);
    delay(50);

    delay( (timeD - timeDelayTotal)*1000 + 100);
    timeDelayTotal = timeD;
  }

  for (int i=5; i<10; i++)
  {
    digitalWrite(i, HIGH);
  }
  delay(1000);
  for (int i=5; i<10; i++)
  {
    digitalWrite(i, LOW);
  }
  delay(1000);


}




