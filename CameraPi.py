import time

import cv2
import picamera
from picamera.array import PiRGBArray

from BaseCamera import BaseCamera


class CameraPi(BaseCamera):

	@staticmethod
	def frames():
		with picamera.PiCamera() as camera:
			camera.resolution = (640, 480)
			#camera.framerate = 32
			rawCapture = PiRGBArray(camera, size=(640, 480))
			time.sleep(2)

			for frame in camera.capture_continuous(rawCapture, 'bgr', use_video_port=True):
				image = frame.array
				image = cv2.flip(image, 0)
				yield cv2.imencode('.jpg', image)[1].tobytes()
				rawCapture.truncate(0)