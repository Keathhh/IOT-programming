// Assigning pin numbers for components
int greenLed = 11;   // Pin number for the green LED
int redLed = 12;     // Pin number for the red LED
int smokeA0 = A0;    // Analog pin number for the smoke sensor
int buzzer = 10;     // Pin number for the buzzer

// Threshold value for smoke detection
int sensorThres = 300;

void setup() {
  // Setting up pin modes
  pinMode(redLed, OUTPUT);    // Sets the red LED pin as an output
  pinMode(greenLed, OUTPUT);  // Sets the green LED pin as an output
  pinMode(buzzer, OUTPUT);    // Sets the buzzer pin as an output
  pinMode(smokeA0, INPUT);    // Sets the smoke sensor pin as an input
  Serial.begin(9600);         // Initializes serial communication at 9600 baud rate
}

void loop() {
  // Reading analog value from the smoke sensor
  int analogSensor = analogRead(smokeA0);

  // Printing analog sensor value to the serial monitor
  Serial.print("Pin A0: ");
  Serial.println(analogSensor);
  delay(1000);  // Delay for 1 second

  // Checking if the analog sensor value exceeds the threshold
  if (analogSensor > sensorThres) {
    // Smoke or fire detected
    digitalWrite(redLed, HIGH);  // Turn on the red LED
    digitalWrite(greenLed, LOW); // Turn off the green LED
    tone(buzzer, 1000, 200);      // Generate a tone on the buzzer
    Serial.println("Fire Detected!");  // Print message to the serial monitor
  } else {
    // No smoke or fire detected
    digitalWrite(redLed, LOW);   // Turn off the red LED
    digitalWrite(greenLed, HIGH);  // Turn on the green LED
    noTone(buzzer);               // Stop the buzzer tone
  }
  delay(100);  // Delay for 100 milliseconds before the next iteration
}
