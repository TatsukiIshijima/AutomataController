import sys
import time
import serial

LED_COMMAND = "led"
DIRECTION_SERVO_COMMAND = "d_servo_"
FORWARD_MOTOR_COMMAND = "f_motor_"
BACKWARD_MOTOR_COMMAND = "b_motor_"
STOP_MOTOR_COMMAND = "s_motor"

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
