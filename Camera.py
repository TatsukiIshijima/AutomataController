import time

import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray


class Camera:

	def __init__(self):
		self.pi_camera = PiCamera()
		self.pi_camera.resolution = (320, 240)
		self.pi_camera.framerate = 24
		self.rawCapture = PiRGBArray(self.pi_camera, size=self.pi_camera.resolution)
		time.sleep(0.5)

	def get_frame(self):
		self.pi_camera.capture(self.rawCapture, format="bgr", use_video_port=True)
		frame = self.rawCapture.array
		ret, jpeg = cv2.imencode('.jpg', frame)
		self.rawCapture.truncate(0)
		return jpeg.tobytes()


if __name__ == '__main__':
	# Cameraの動作確認
	camera = Camera()
	camera.pi_camera.capture('test_picture.jpg')
