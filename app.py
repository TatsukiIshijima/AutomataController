import json
import signal
import sys

from flask import Flask, render_template, redirect, url_for, request, jsonify, Response

from CameraPi import CameraPi
from PiClient import PiClient

app = Flask(__name__)
pi_client = PiClient()


@app.route('/', methods=['GET'])
def form():
	return redirect(url_for('home'))


@app.route('/home', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		if request.form.get('Forward') == 'Forward':
			forward()
		elif request.form.get('Backward') == 'Backward':
			backward()
		elif request.form.get('Left') == 'Left':
			turn_left()
		elif request.form.get('Right') == 'Right':
			turn_right()
		elif request.form.get('Stop') == 'Stop':
			stop()
	return render_template('home.html')


def _execute(func):
	response = {
		'result': False,
		'message': ''
	}
	if request.method == 'POST':
		func
		response['result'] = True
	return jsonify(json.dumps(response))


@app.route('/home/led', methods=['POST'])
def led():
	_execute(pi_client.launch_led())


@app.route('/home/forward', methods=['POST'])
def forward():
	_execute(pi_client.accelerate(60))


@app.route('/home/backward', methods=['POST'])
def backward():
	_execute(pi_client.accelerate(60, False))


@app.route('/home/turn_left', methods=['POST'])
def turn_left():
	_execute(pi_client.turn(60))


@app.route('/home/turn_right', methods=['POST'])
def turn_right():
	_execute(pi_client.turn(90))


@app.route('/home/stop', methods=['POST'])
def stop():
	_execute(pi_client.accelerate(0))
	_execute(pi_client.turn(75))


def handler(signal, frame):
	print('Application finished. (CTRL+C pressed)')
	pi_client.close()
	sys.exit()


@app.route('/stream')
def stream():
	return Response(generate(CameraPi()),
	                mimetype='multipart/x-mixed-replace; boundary=frame')


def generate(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
	           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

'''
def __update_drive_error(response):
	if response is not None:
		flash(f'{response.message}')
'''

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=80)
	signal.signal(signal.SIGINT, handler)
	signal.pause()
