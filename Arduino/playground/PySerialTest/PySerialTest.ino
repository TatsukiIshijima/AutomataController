#include <SoftwareSerial.h>

// RaspiのGPIO14(TXD0) - Arduino PIN 5(RXとする)
// RaspiのGPIO15(RXD0) - Arduino PIN 6(TXとする)
 
const int SERIAL_PIN_RX = 5;
const int SERIAL_PIN_TX = 6;
const int LED_PIN = 13;

SoftwareSerial ser(SERIAL_PIN_RX, SERIAL_PIN_TX);

boolean ledOn = false;

void setup() {
  ser.begin(9600);
  
  // シリアルモニタ用
  Serial.begin(9600);
  Serial.println("Serial Start");
  
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // シリアルモニタ用
  /*
  if (Serial.available()) {
    String inputStr = Serial.readStringUntil(';');
    Serial.println(inputStr);
    if (inputStr.equals("led")) {
      toggleLED();
      Serial.println("toggle LED");
    }
  }
  */
  
  if (ser.available()) {
    String inputStr = ser.readStringUntil(';');
    Serial.println(inputStr);
    if (inputStr.equals("led")) {
      Serial.println("toggle LED");
      toggleLED();
    } else {
      Serial.println(inputStr);
    }
  }
}

void toggleLED() {
  ledOn = !ledOn;
  digitalWrite(LED_PIN, ledOn);
}
