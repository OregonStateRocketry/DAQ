// Reads analog voltage values and prints them to serial.
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
}

void loop() {
  // read the input on analog pin 0:
  int loadCellVal = analogRead(A0);
  int PTval = analogRead(A7);
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  double loadCellVoltage = loadCellVal * (5.0 / 1023.0);
  double loadCellLbf = (402.88)*(loadCellVoltage) - 43.59;
  double PTvoltage = (PTval) * (5.0 / 1023.0);
  double pressure_psi = (1225.4*(PTvoltage) - 806.075);
  // print out the value you read:
  Serial.print(loadCellLbf);
  Serial.print(",");
  Serial.println(pressure_psi);
}
