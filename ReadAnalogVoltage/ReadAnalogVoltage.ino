// Reads analog voltage values and prints them to serial.
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

void loop() {
  // read the input on analog pin 0:
  int loadCellVal = analogRead(A0);
  int PTvalmin = analogRead(A7);
  int PTvalmax = analogRead(A6);
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float loadCellVoltage = loadCellVal * (5.0 / 1023.0);
  float PTvoltage = (PTvalmax - PTvalmin) * (5.0 / 1023.0);
  // print out the value you read:
  Serial.print(loadCellVoltage);
  Serial.print(",");
  Serial.println(PTvoltage);
}
