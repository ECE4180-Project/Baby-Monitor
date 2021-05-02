from flask import Flask, render_template, jsonify, request, Response
from datetime import datetime
from pydub import AudioSegment
from camera_pi import Camera
from subprocess import Popen, PIPE
import threading
import os
import pygame
import pyaudio
import time
import sys

app = Flask(__name__)
BASE_DIR = '/home/pi/Desktop/simplerecorder/Audio_Files'

pygame.init()

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 8192
RECORD_SECONDS = 5


audio1 = pyaudio.PyAudio()



disturbance_count = str(0)


p = Popen(['-u','sudo ./FilterVersion','-o0'], shell=True, stdout=PIPE, stdin=PIPE, bufsize = 0,)


def getsonar():
    global disturbance_count
    return str(disturbance_count)

def getdisturbance():
    #threading.Timer(0.25, getdisturbance).start()
    while True:
        global disturbance_count
        disturbance_count = str(p.stdout.readline())
        #print("ThreadRun  " + disturbance_count)
        
        time.sleep(0.25)
    
disturbancethread = threading.Thread(target=getdisturbance)
disturbancethread.start()


def to_bytes(n, length, endianess ='big'):
    h = '%x' % n
    s = ('0'*(len(h) % 2) + h).zfill(length*2).decode('hex')
    return s if endianess == 'big' else s[::-1]


def genHeader(sampleRate, bitsPerSample, channels):
    datasize = 2000*10**6
    #o = bytes("RIFF",encoding=['ascii'])                                               # (4byte) Marks file as RIFF
    o = str('RIFF').encode('ascii')
    #o += (datasize + 36).to_bytes(4,'little')                               # (4byte) File size in bytes excluding this and RIFF marker
    o += to_bytes((datasize + 36),4,'little')
    #o += bytes("WAVE",'ascii')                                              # (4byte) File type
    o += str('WAVE').encode('ascii')
    #o += bytes("fmt ",'ascii')                                              # (4byte) Format Chunk Marker
    o += str("fmt ").encode('ascii')
    #o += (16).to_bytes(4,'little')                                          # (4byte) Length of above format data
    o += to_bytes(16,4,'little')
    #o += (1).to_bytes(2,'little')                                           # (2byte) Format type (1 - PCM)
    o += to_bytes(1, 2, 'little')
    #o += (channels).to_bytes(2,'little')                                    # (2byte)
    o += to_bytes(channels,2,'little')
    #o += (sampleRate).to_bytes(4,'little')                                  # (4byte)
    o += to_bytes(sampleRate,4,'little')
    #o += (sampleRate * channels * bitsPerSample // 8).to_bytes(4,'little')  # (4byte)
    o += to_bytes((sampleRate * channels * bitsPerSample // 8),4,'little')
    #o += (channels * bitsPerSample // 8).to_bytes(2,'little')               # (2byte)
    o += to_bytes((channels * bitsPerSample //8),2, 'little')
    #o += (bitsPerSample).to_bytes(2,'little')                               # (2byte)
    o += to_bytes(bitsPerSample, 2, 'little')
    #o += bytes("data",'ascii')                                              # (4byte) Data Chunk Marker
    o += str('data').encode('ascii')
    #o += (datasize).to_bytes(4,'little')                                    # (4byte) Data size in bytes
    o += to_bytes(datasize, 4, 'little')
    return o

@app.route('/audio')
def audio():
    # start Recording
    def sound():

        CHUNK = 8192
        sampleRate = 44100
        bitsPerSample = 16
        channels = 1
        wav_header = genHeader(sampleRate, bitsPerSample, channels)

        stream = audio1.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,input_device_index=2,
                        frames_per_buffer=CHUNK)
        print("recording...")
        #frames = []
        first_run = True
        while True:
           if first_run:
               data = wav_header + stream.read(CHUNK)
               first_run = False
           else:
               data = stream.read(CHUNK)
           yield(data)

    return Response(sound())

def play_music(pathid):
    my_sound = pygame.mixer.Sound(pathid)
    my_sound.play()

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        f = request.files['audio_data']
        with open('audio.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')

        return render_template('index.html', request="POST")
    else:
        return render_template("index.html",variable = getsonar())
  

@app.route('/save_audio/', methods=["POST"])
def save_audio():

    file = request.files['audio_data']
    filename = datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + '.wav'

    file.save(os.path.join(BASE_DIR, filename))
    filepath = '/home/pi/Desktop/simplerecorder/Audio_Files/' + str(filename)
    music_thread = threading.Thread(target=play_music, args=([filepath]))
    music_thread.start()
    
    print(BASE_DIR + filename)

    return jsonify({"status": True})




@app.route('/upload', methods =["POST"])
def upload():
    file = request.files['audio_data']
    print('file received')
    return file.filename




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




if __name__ == '__main__':
    
    if not os.path.exists(directory):
        os.makedirs(BASE_DIR)
    app.run(host='0.0.0.0', ssl_context=('cert.pem', 'key.pem'))

