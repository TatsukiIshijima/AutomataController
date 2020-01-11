import sys
import time

import serial

if __name__ == '__main__':

	ser = serial.Serial('/dev/ttyS0', 9600, timeout=5, write_timeout=3)
	time.sleep(2)

	while True:
		command = input("Enter command: led; - toggle LED, e - exit ")
		if command == 'led;':
			ser.write(command.encode('utf-8'))
		elif command == 'e':
			print('System exit.')
			break

	ser.close()
	sys.exit()
