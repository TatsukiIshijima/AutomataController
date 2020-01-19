from flask import Flask, render_template, redirect, url_for, request, Response

from Camera import Camera

app = Flask(__name__)


@app.route('/', methods=['GET'])
def form():
	return redirect(url_for('home'))


@app.route('/home', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		if request.form.get('Forward') == 'Forward':
			print('Forward')
		elif request.form.get('Backward') == 'Backward':
			print('Backward')
		elif request.form.get('Left') == 'Left':
			print('Lef')
		elif request.form.get('Right') == 'Right':
			print('Right')
		elif request.form.get('Stop') == 'Stop':
			print('Stop')
	return render_template('home.html')


@app.route('/stream')
def stream():
	return Response(generate(Camera()),
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
