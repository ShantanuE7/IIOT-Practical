// Define the PIR sensor and LED pins
const int pirSensorPin = A0;    // PIR sensor is connected to analog pin A0
const int ledPin = 13;          // Built-in LED pin on Arduino

void setup() {
  pinMode(pirSensorPin, INPUT); // Set PIR sensor pin as input
  pinMode(ledPin, OUTPUT);      // Set LED pin as output
  Serial.begin(9600);           // Initialize serial communication for debugging
}

void loop() {
  int pirValue = analogRead(pirSensorPin); // Read the analog value from the PIR sensor
  Serial.print("PIR Value: ");
  Serial.println(pirValue);                // Print PIR sensor value to Serial Monitor

  if (pirValue > 512) {                    // Assuming a threshold to detect motion
    digitalWrite(ledPin, HIGH);            // Turn on LED if motion is detected
  } else {
    digitalWrite(ledPin, LOW);             // Turn off LED if no motion
  }

  delay(500); // Wait half a second before the next read
}
