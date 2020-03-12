import sys
import time

import serial
from serial.tools import list_ports

LED_COMMAND = "led"
DIRECTION_SERVO_COMMAND = "d_servo_"
FORWARD_MOTOR_COMMAND = "f_motor_"
BACKWARD_MOTOR_COMMAND = "b_motor_"
STOP_MOTOR_COMMAND = "s_motor"


class PiClient:

	def __init__(self):
		self._ser = serial.Serial()
		self._ser.port = '/dev/serial0'
		self._ser.baudrate = 9600
		self._ser.timeout = 1
		self._ser.write_timeout = 1
		self._ports = list_ports.comports()
		self._devices = [info.device for info in self._ports]
		if len(self._devices) != 1:
			print('error : device not found.')
			sys.exit()
		print('device found %s' % self._devices[0])
		try:
			self._ser.open()
			time.sleep(1)
		except:
			print('error : can not open serial.')
			sys.exit()

	def _write(self, command_str):
		if self._ser.is_open:
			self._ser.write(command_str.encode('utf-8'))

	def launch_led(self):
		self._write(LED_COMMAND + ';')

	def accelerate(self, power, is_forward=True):
		if power < 0 or power > 255:
			return
		elif power == 0:
			self._write(STOP_MOTOR_COMMAND + ';')
		else:
			if is_forward:
				self._write(FORWARD_MOTOR_COMMAND + str(power) + ';')
			else:
				self._write(BACKWARD_MOTOR_COMMAND + str(power) + ';')

	def turn(self, direction):
		if direction < 0 or direction > 180:
			return
		self._write(DIRECTION_SERVO_COMMAND + str(direction) + ';')

	def close(self):
		self._ser.close()


if __name__ == '__main__':

	ser = serial.Serial('/dev/serial0', 9600, timeout=5, write_timeout=3)
	print("-------------------- Device Control ----------------------")
	print("COMMAND LIST")
	print("1. led        - Arduino pro mini 13 pin led light up or down.")
	print("2. d_servo_90 - Servo motor degree.")
	print("3. f_motor_60 - DC motor forward.")
	print("4. b_motor_60 - DC motor backward.")
	print("5. s_motor    - DC motor stop.")
	print("6. e          - exit")
	print("----------------------------------------------------------")
	time.sleep(2)

	while True:
		command = input("Enter command: ")
		# LED
		if command == LED_COMMAND:
			led_command = LED_COMMAND + ";"
			ser.write(led_command.encode('utf-8'))
		# 方向サーボ
		elif command.startswith(DIRECTION_SERVO_COMMAND):
			if len(command.split("_")) == 3:
				try:
					degree = int(command.split("_")[2])
					if degree < 0 or degree > 180:
						print("Waring : input degree out of range. (0 ~ 180)")
						continue
					d_servo_command = DIRECTION_SERVO_COMMAND + str(degree) + ";"
					ser.write(d_servo_command.encode('utf-8'))
				except ValueError:
					print("Cast Error : input string(degree) is not integer number or empty.")
					break
		# モーター前転
		elif command.startswith(FORWARD_MOTOR_COMMAND):
			if len(command.split("_")) == 3:
				try:
					speed = int(command.split("_")[2])
					if speed < 0 or speed > 255:
						print("Waring : input speed out of range.(0 ~ 255)")
						continue
					f_motor_command = FORWARD_MOTOR_COMMAND + str(speed) + ";"
					ser.write(f_motor_command.encode('utf-8'))
				except ValueError:
					print("Cast Error : input string(speed) is not integer number or empty.")
					break
		# モーター後転
		elif command.startswith(BACKWARD_MOTOR_COMMAND):
			if len(command.split("_")) == 3:
				try:
					speed = int(command.split("_")[2])
					if speed < 0 or speed > 255:
						print("Waring : input speed out of range.(0 ~ 255)")
						continue
					f_motor_command = BACKWARD_MOTOR_COMMAND + str(speed) + ";"
					ser.write(f_motor_command.encode('utf-8'))
				except ValueError:
					print("Cast Error : input string(speed) is not integer number or empty.")
					break
		# モーター停止
		elif command.startswith(STOP_MOTOR_COMMAND):
			stop_motor_command = STOP_MOTOR_COMMAND + ";"
			ser.write(stop_motor_command.encode('utf-8'))
		elif command == "e":
			print("System exit.")
			break

	ser.close()
	sys.exit()
