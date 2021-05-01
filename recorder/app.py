from flask import Flask, render_template, jsonify, request, Response
from datetime import datetime

from camera_pi import Camera

import os

app = Flask(__name__)
BASE_DIR = 'audio_files/'


@app.route('/')
def index():
    return render_template('./index.html')
    
def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/save_audio/', methods=["POST"])
def save_audio():

    file = request.files['audio_data']
    filename = datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + '.wav'

    file.save(os.path.join(BASE_DIR, filename))

    print(BASE_DIR + filename)

    return jsonify({"status": True})


if __name__ == '__main__':
    
    if not os.path.exists(directory):
        os.makedirs(BASE_DIR)
    #app.run(host='0.0.0.0', port = '7600',ssl_context=('cert.pem', 'key.pem'))
    app.run(host=args["ip"], port=args["port"], debug=True,
		threaded=True, use_reloader=False)
