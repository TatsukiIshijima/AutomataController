import time
from enum import Enum

import RPi.GPIO as GPIO


class Color(Enum):
	GREEN = 17
	YELLOW = 18
	BLUE = 22
	WHITE = 27


class LED:
	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(Color.GREEN.value, GPIO.OUT)
		GPIO.setup(Color.YELLOW.value, GPIO.OUT)
		GPIO.setup(Color.BLUE.value, GPIO.OUT)
		GPIO.setup(Color.WHITE.value, GPIO.OUT)

	def switch_power(self, color, is_on):
		power = 1 if is_on else 0

		if color == Color.GREEN:
			GPIO.output(Color.GREEN.value, power)
		elif color == Color.YELLOW:
			GPIO.output(Color.YELLOW.value, power)
		elif color == Color.BLUE:
			GPIO.output(Color.BLUE.value, power)
		elif color == Color.WHITE:
			GPIO.output(Color.WHITE.value, power)
		else:
			print('SyntaxError: invalid syntax , not support led color.')

	def __del__(self):
		GPIO.cleanup(Color.GREEN.value)
		GPIO.cleanup(Color.YELLOW.value)
		GPIO.cleanup(Color.BLUE.value)
		GPIO.cleanup(Color.WHITE.value)


if __name__ == '__main__':
	led = LED()
	led.switch_power(Color.GREEN, True)
	time.sleep(1)
	led.switch_power(Color.GREEN, False)
	time.sleep(1)
	led.switch_power(Color.YELLOW, True)
	time.sleep(1)
	led.switch_power(Color.YELLOW, False)
	time.sleep(1)
	led.switch_power(Color.BLUE, True)
	time.sleep(1)
	led.switch_power(Color.BLUE, False)
	time.sleep(1)
	led.switch_power(Color.WHITE, True)
	time.sleep(1)
	led.switch_power(Color.WHITE, False)
	time.sleep(1)
	del led
