import time

import RPi.GPIO as GPIO

DC_MOTOR_GPIO = 19

if __name__ == '__main__':
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(DC_MOTOR_GPIO, GPIO.OUT)

	servo = GPIO.PWM(DC_MOTOR_GPIO, 50)

	servo.start(0)
	time.sleep(1)

	angle = (12 - 2.5) / 180
	for i in range(180):
		servo.ChangeDutyCycle(2.5 + i * angle)
		time.sleep(0.1)

	for i in range(180):
		servo.ChangeDutyCycle(12 - i * angle)
		time.sleep(0.1)

	servo.stop()
	GPIO.cleanup()
