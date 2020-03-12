#include <Servo.h>
#include <SoftwareSerial.h>

// Servo.hライブラリを使用すると9, 10ピンのPWMが機能しなくなるので注意
// RaspiのGPIO14(TXD0) - Arduino PIN 5(RXとする)
// RaspiのGPIO15(RXD0) - Arduino PIN 6(TXとする)
 
#define SERIAL_PIN_RX 5
#define SERIAL_PIN_TX 6
#define DIRECTION_SERVO_PIN 9
#define PWMA 3
#define AIN2 11
#define AIN1 12
#define LED_PIN 13

const String LED_COMMAND = "led";
const String DIRECTION_SERVO_COMMAND = "d_servo_";
const String FORWARD_MOTOR_COMMAND = "f_motor_";
const String BACKWARD_MOTOR_COMMAND = "b_motor_";
const String STOP_MOTOR_COMMAND = "s_motor";

Servo directionServo;
SoftwareSerial piSerial(SERIAL_PIN_RX, SERIAL_PIN_TX);

boolean ledOn = false;

void setup() {
  piSerial.begin(9600);

  // シリアルモニタ用（デバッグ用）
  Serial.begin(9600);
  Serial.println("Serial Start");

  pinMode(PWMA, OUTPUT);
  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);
  pinMode(LED_PIN, OUTPUT);

  directionServo.attach(DIRECTION_SERVO_PIN);
  changeAngle(75);
  stopMotor();
}

void loop() {
  
  // デバッグ用
  //if (Serial.available()) {
    //String inputCommand = Serial.readStringUntil(';');
  
  // 本番用
  if (piSerial.available()) {
    String inputCommand = piSerial.readStringUntil(';');

    // LED
    if (inputCommand.equals(LED_COMMAND)) {
      Serial.println("toggle LED");
      toggleLED();
    
    // 方向用サーボ  
    } else if (inputCommand.startsWith(DIRECTION_SERVO_COMMAND)) {
      // コマンド文字列「d_servo_」の8文字を削除
      String degreeString = inputCommand.substring(8);
      degreeString.replace(";", "");
      int degree = degreeString.toInt();
      changeAngle(degree);
      Serial.println(degree);
    
    // モーター前転  
    } else if(inputCommand.startsWith(FORWARD_MOTOR_COMMAND)) {
      // コマンド文字列「f_motor_」の8文字を削除
      String speedString = inputCommand.substring(8);
      int motorSpeed = speedString.toInt();
      startMotor(true, motorSpeed);
      Serial.println("forward motor");
    
    // モーター後転
    } else if(inputCommand.startsWith(BACKWARD_MOTOR_COMMAND)) {
      // コマンド文字列「b_motor_」の8文字を削除
      String speedString = inputCommand.substring(8);
      int motorSpeed = speedString.toInt();
      startMotor(false, motorSpeed);
      Serial.println("backward motor");
    
    // モーターストップ
    } else if(inputCommand.startsWith(STOP_MOTOR_COMMAND)) {
      stopMotor();
      Serial.println("stop motor");
      
    } else {
      Serial.println(inputCommand);
    }
  }
}

// Arduino付属のLEDのオンオフ（デバッグ用）
void toggleLED() {
  ledOn = !ledOn;
  digitalWrite(LED_PIN, ledOn);
}

// Servoの向き変更
void changeAngle(int angle) {
  if (angle < 0 || angle > 180) {
    return;
  }
  directionServo.write(angle);
}

// モーター前転・後転
void startMotor(bool isForward, int speedValue) {
  if (speedValue < 0 || speedValue > 255) {
    return;
  }
  if (isForward) {
    digitalWrite(AIN1, HIGH);
    digitalWrite(AIN2, LOW);
  } else {
    digitalWrite(AIN1, LOW);
    digitalWrite(AIN2, HIGH);
  }
  analogWrite(PWMA, speedValue);
}

// モーター停止
void stopMotor() {
  analogWrite(PWMA,0);
  digitalWrite(AIN1,LOW);
  digitalWrite(AIN2,LOW);
}
