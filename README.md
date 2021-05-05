# Baby Monitor
######  by Erobhosele Sado, Sidney Wise, Jack Darrow, and  Ben Nixon  

## Summary
Do you worry about not being able to hear or speak to your baby through a traditional baby monitor at night? want to live stream video of you child from any of your devices? Try building our Raspberry Pi-based baby monitor! This baby monitor allows for parents to view a live video stream of their child over a local area network. This monitor also allows worrying parents to listen in and talk to their baby over any device on the same network!

<p align="center">
  <img src="https://github.com/ECE4180-Project/Baby-Monitor/blob/82f1b7d4552be3f108e9d4ff8998643f9644ffcf/monitor.JPG" width=60% height=60% >
</p>

## Video Demonstration

[![ Video Demonstration](https://img.youtube.com/vi/SIyJqpgRfIs/hqdefault.jpg)](https://www.youtube.com/embed/SIyJqpgRfIs) </br>

https://www.youtube.com/watch?v=SIyJqpgRfIs </br>


## Presentation

[![ Video Presentation](https://img.youtube.com/vi/N9WD8GG3MUE/hqdefault.jpg)](https://www.youtube.com/embed/N9WD8GG3MUE) </br>


https://www.youtube.com/watch?v=N9WD8GG3MUE

## Parts
- Raspberry Pi 3 
- MicroUSB cable and wall adapter
- Monitor or display with appropriate cables to connect to the Pi
- Raspberry Pi NoIR Camera V2 with ribbon cable
- HC-SR04 Sonar Sensor
- USB Microphone
- Speaker with 2.1mm jack input 
- Male to female jumper wires

# How It Works
## Block Diagram

<p align="center">
  <img src="https://github.com/ECE4180-Project/Baby-Monitor/blob/8d8d51cf6e33146298be55a935a2896a21d9d9df/block_diagram.JPG" width=70% height=70% >
</p>


## File Structure
- For reference, the file structure is shown below.
```
    ├── Desktop
       ├── code
            ├── app.py
            ├── camera_pi.py
            ├── FilterVersion.cpp
            ├── FilterVersion
            ├── cert.pem
            ├── key.pem
            ├── Pi_Monitor_4180
            ├── templates
	    |    └── index.html
            ├── Audio_Files
	    └── Static
	       	 ├── css
		 |    └── style.css   
		 └── js
		      ├── app.js
		      ├── justgage.js
		      └── raphael-2.1.4.min.js 

```

## Setting Up the Hardware
- Connect the HC-SR04 Sonar Sensor to the Raspberry Pi 3
    - The HC-SR04 is powered using the Arduino Uno's 5V and GND pins, and operates using two GPIO pins. The two GPIO pins used in this process are GPIO pins 14 and 15.
    - The schematic below shows how to connect the HC-SR04 sensor using male to female dual head jumper wires.
- Connect the Raspberry Pi to a monitor or display. For this instance, the Pi was connected to a monitor using HDMI.
- Plug the USB microphone into the Pi.
- Connect a USB keyboard and mouse to the Pi.
- Attach a speaker to the Pi through the 2.1mm headphone jack.

<p align="center">
  <img src="https://github.com/ECE4180-Project/Baby-Monitor/blob/b9081051db8c2454694235fefee88f3ce7e8a243/PiWiringDiagram.JPG" width=100% height=100% >
</p>
<p align="center">
  Wiring Diagram
</p>


- Below is a table of connections between the HC-SR04 and the Raspberry Pi.

| Sonar  | Raspberry pi |
| ------------- | ------------- |
| Vcc  | 5V |
| Gnd | Gnd |
| trig | pin 14 |
| echo | pin 15  |


## Camera, Recorder & Server Setup 
- Connect the Pi to the local area network with internet access that you want to use the monitor on.
- Download the files and save onto the Pi's desktop.
- To setup the camera first user must enable it on the Pi by going to **Preferences->Raspberry Pi Configuration-> Interfaces**, then reboot the Pi
- Next, download these modules in order to run the camera, recorder, and server.
```
sudo apt-get install python3-flask
sudo apt-get install pydub
sudo apt-get install pyaudio
sudo apt-get install openssl

```
- After installation is complete, create a SSL certificate and key using openssl. Type in the line below, and follow the instructions.
```
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout -key.pem -days 365
```
- When the SSL certificate and key are generated, run the server using the command below.
```
flask run --cert=cert.pem --key=key.pem --host=0.0.0.0
```
- Hover the Pi's pointer over the internet connection logo in the toolbar. The IP address for the Pi should appear.
- On another device connected to the same local area network, such as a laptop or smartphone, go to the web browser, and type in the Pi's IP address followed by the port number 5000 as shown in the example below.
```
https://10.136.0.186:5000/
```
- Ignore any warnings the browser brings up about the connection being unsafe. Continue to the website.
- Your web browser should bring up the page shown below. Now you can begin using your new baby monitor!

<p align="center">
  <img src="https://github.com/ECE4180-Project/Baby-Monitor/blob/f36eec5f5bcfc181cdca8aa1eb4bd89dbe4253fb/Screenshot%20from%202021-05-03%2021-06-15.png" width=100% height=100% >
</p>

- At the top of the page are audio controls to speak to the baby. When you want to say something, press record, speak your message, and then hit stop. 
- Hitting stop automatically plays the message for the baby on the monitor's speaker. 
- After you hit record, you can also speak, hit pause to think about what you are going to say next, and then continue speaking by hitting record again.
- Below the three control buttons is a live video feed from the monitor. 
- If you scroll down to the bottom of the page, you will find a gauge graphic labeled "Baby's Movement"
- This graphic shows you how active your baby has been throughout the night by displaying the number of large movements that have occured throughout the night.
<p align="center">
  <img src="https://github.com/ECE4180-Project/Baby-Monitor/blob/f36eec5f5bcfc181cdca8aa1eb4bd89dbe4253fb/Screenshot%20from%202021-05-03%2021-09-09.png" width=100% height=100% >
</p>

- At the very bottom of the page is another set of audio controls. These controls are for sound being fed from the monitor's USB microphone to the server page. Pressing the 'play' button play audio from the monitor on your device.

## Sonar Detection
<p align="center">
  <img src="https://user-images.githubusercontent.com/82454615/116896397-34c26800-ac02-11eb-8a26-f865a4ca29db.png" width=30% height=30% >
</p>
<p align="center">
  HCSR04 from Sparkfun
</p>

- The baby's movement is tracked using the HC-SR04 Sonar Sensor.  
- The sonar operates by sending out a pulse and then measuring how long it takes for the entire pulse to bounce off an object an return to the sensor.  
- The time it takes for the pulse to bounce off an object and return is dependent upon how far away the object is.  

<p align="center">
  <img src="https://github.com/ECE4180-Project/Baby-Monitor/blob/420617f118cf526631bc26cf15c79aee5247c440/arduino-ultrasonic-distance-sensor4.png" width=50% height=50% >
</p>
<p align="center">
  HCSR04 Timing Diagram from  https://www.javatpoint.com/arduino-ultrasonic-distance-sensor
</p>



- For the Pi to operate the sonar, a custom class called "sonar" was made that utilizes the PIGPIO library (http://abyz.me.uk/rpi/pigpio/). This class takes in an integer number for the sonar's trigger pin, an integer number for the sonar's echo pin, and if desired, a long integer number that represents the desired timeout delay for the sonar.
- Within the class is a function called "distance." the distance function will return the distance from the sonar to an object.
    - The distance function starts by storing the current number of microseconds since system boot in the "trackTick" variable. This variable is used in the event a custom timeout value is set.
  ```
   // GPIO tick used for timout purposes.
  trackTick = gpioTick();
  ```
    - Next, the PIGPIO library is used to set the GPIO level on the trigger pin to LOW for two microseconds. Then, the GPIO level on the trigger pin is set high for 10 microseconds, and then set LOW again. This creates the ultrasonic pulse.
  ```
   // Set the trigger pin low for 2 microseconds, high for 10 microseconds, and then low again.
   gpioWrite(triggergpio, PI_OFF);
   gpioDelay(2);
   gpioWrite(triggergpio, PI_ON);
   gpioDelay(10);
   gpioWrite(triggergpio, PI_OFF);
  ```
    - The receiver portion of the HC-SR04 then waits for the ultrasonic pulse to bounce back. When the sensor detects the beginning of the waveform returning to the sensor, the PIGPIO libary will read a high value on the echo pin, and the program will mark the current time in microseconds since system boot.
    - After the entire waveform has returned to the sonar, the PIGPIO library will read a low value on the echo pin, and the program will once again mark the time since system boot. 
    ```
   // Continuously set startTick to the current tick until the echo pin goes high (receive signal) or time expires.
  while(gpioRead(echogpio) == 0 && (gpioTick() < (trackTick + timeout))){
	  startTick = gpioTick();
  }
  // Continuously update set endTick to the current tick while the echo pin is high.
  while(gpioRead(echogpio) == 1){
	 endTick = gpioTick();
  }
  ```
    - The difference in time since system boot at the start of the waveform and at the end of the waveform is found. 
  ```
   diffTick = endTick - startTick;
  if(diffTick > timeout){
      diffTick = timeout;
  }
  return ((int) diffTick);
  }
  ```
    - This time difference decreases as an object gets closer to the sonar and increases as an object gets farther away from the sonar.

## Creating a Disturbance Metric
- To create a metric that effectively communicates how active the baby is, some basic statistics are used to analyze data from the sonar.
- The program "FilterVersion.cpp" both obtains and analyzes the sonar data using a continous loop that executes once every 0.25 seconds.
- The the main function of the program starts by initilizing the PIGPIO library, creating a length 100 data array to continuously store the latest sonar data, and initializing all the values in this array to 0.
- The program then enters a "while" loops that runs indefinitely. 
- The loop starts by shifting all data array values down by one place to make room for the newest data value.
- An instance of the sonar class is used to determine the current distance the baby is from the sensor. This new data value is then added to the data array.
- The average value of the length 100 data array is calculated. This average value is used along with the 100 data values to calculate the current standard deviation of the 100 distance data values.
<p align="center">
  <img src="https://github.com/ECE4180-Project/Baby-Monitor/blob/e700ed8024377659e5ff1ae42fa3679e5c16c1c7/average.JPG" width=50% height=50% >
</p>
<p align="center">
	Formula for Calculating the Average
</p>
<p align="center">
  <img src="https://github.com/ECE4180-Project/Baby-Monitor/blob/9124d259437d95bef4ceae3b513ce624c436176c/standard_deviation.JPG" width=50% height=50% >
</p>
<p align="center">
	Formula for Calculating the Standard Deviation
</p>

- Next, the current distance value is analyzed. if the current distance is greater than the current mean plus two times the standard deviation, or less than the mean minus two times the standard deviation, a disturbance count variable is incremented by one.
- This disturbance count value is then written to the standard output stream, and the data measurement and analysis process starts again.
- This process is completed once every 0.25 seconds indefinitely.
- In order to prevent the initial startup of the sensor from generating false disturbances, there is logic in place to prevent the disturbance count value from being incremented until 125 measurements have been taken.
## Sending Sonar Data to the Server Page
- Our sonar data is being written to the standard output stream. Now, we must bring this data into our main Python program, "app.py".
- To get our sonar data into the Python program we will use a pipe. Pipes are used to pass information from one program to another. The information passed from one process through the pipe is held until accessed, so our program must read in data as fast as it is put into the pipe in order to prevent a backlog.
- The line of code below imports elements from the subprocess module that we will be using.
  ```
   from subprocess import Popen, PIPE
  ```
- Now, we will open a pipe to the sonar executable file created earlier, and execute the file as a child process.
 ```
   p = Popen(['-u','sudo ./FilterVersion','-o0'], shell=True, stdout=PIPE, stdin=PIPE, bufsize = 0,)
  ```
 - When 'app.py' runs, it will now start the C++ code for the sonar. Next, we have to bring in data from the pipe at the same rate it is generated.
 - A function is used to update a global value in 'app.py' with the latest sonar data. A thread is used to call this function once every 0.25 seconds, matching the rate at which data is put into the pipe by the child process.
 ```
   def getdisturbance():
    #threading.Timer(0.25, getdisturbance).start()
    while True:
        global disturbance_count
        disturbance_count = str(p.stdout.readline())
        #print("ThreadRun  " + disturbance_count)
        
        time.sleep(0.25)
    
disturbancethread = threading.Thread(target=getdisturbance)
disturbancethread.start()
  ```
  - Now that we have the disturbance count being piped into our Python program, we can edit the 'index.html' file to display this data using a gauge graphic.
  - To make our gauge graphic, we wil use a Javascript plugin called 'JustGage.' This plugin uses a Javascript library called 'Raphael.' You can find both of these files at the JustGage github page: https://toorshia.github.io/justgage/
  - After downloading the both and placing these files in the 'js' folder of the file structure, we can add a gauge to our server page.
  - Add the following lines to the body of the 'index.html' file. This code will create a new gauge graphic. The graphic takes in the disturbance count value fed in from the 'app.py' Python program, and then draws a gauge graphic to give the parent a visual representation of how active the child is.

<p align="center">
  <img src="https://github.com/ECE4180-Project/Baby-Monitor/blob/0d4748b0026c3e64751569f518b802241e89b70f/gauge.JPG" width=50% height=50% >
</p>

## Starting the Server
- Flask is used to create the server.
- Flask is a Python module that makes developing web applications simple and easy.
- You can learn more about Flask and see basic server setups at https://flask.palletsprojects.com/en/1.1.x/
- Like all Flask servers, our server starts off by instantiating the app in the main Python file called "app.py."
  ```
   from flask import Flask
   app = Flask(__name__)
  ```
- After the instantiation, various functions and app routes are implemented that will be discussed later.
- At the end of "app.py," the server starts when teh following segment of code runs.
  ```
   if __name__=='__main':
   	if not os.path.exists(directory):
		os.makedirs(BASE_DIR)
	app.run(host = '0.0.0.0', ssl_context=('cert.pem', 'key.pem'), debug = False)
  ```
- Flask applications use a specific file structure to organize different files. See the file structure at the top of the page.
## Streaming the Camera
- To stream the camera, we will be using Marcelo Rovai's camera class. This class can be found on his GitHub at https://github.com/Mjrovai/Video-Streaming-with-Flask/blob/master/camWebServer/camera_pi.py
- We also implement several app routes and functions in "app.py" that Marcelo has developed for streaming a Pi camera to a server.
	- The "gen" function is used to countinously grab frames from the cameraand the 'video_feed' app route is used to route this stream to the server page.
- Now that we have the Python code in place to stream the camera, we can add it to our server page by altering the "index.html" file.
	- In the body of the "index.html" file, add the image source.
  ```
   <h3><img src="{{ url_for('video_feed') }}" width = 80%></h3>
  ```
- Changing the percentage value in the line above will adjust the size of the video window on the server page.
## Sending Audio from the Parent's Device to the Baby Monitor
- To stream audio from the Parent's device to the baby monitor, a modified version of AddPipe's simplerecorder application developed using Matt Diamond's recorder.js Javascript Plugin. You can find AddPipe's application at the following link: https://github.com/addpipe/simple-recorderjs-demo
- The Javascript code used for recording audio from the parent and sending to the monitor can be found in the "app.js" file.
- With "app.js" in the javascript file directory, we can add functions and app routes to the main Python program "app.py."
	- We will modify the "/" app route to include 'POST' and 'GET' methods to allow for data to be sent to and from the server.
	- A new app route called "save_audio" is added. The function attached to this route will request audio data files, modify the file name, save the file in a folder, and then start a thread that plays the audio file using the pygame library.
     ```
	@app.route('/save_audio/', methods=["POST"])
	def save_audio():

    	file = request.files['audio_data']
    	filename = datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + '.wav'

    	file.save(os.path.join(BASE_DIR, filename))
    	filepath = '/home/pi/Desktop/simplerecorderwithgage/Audio_Files/' + str(filename)
    	music_thread = threading.Thread(target=play_music, args=([filepath]))
    	music_thread.start()
    
    	print(BASE_DIR + filename)

   	 return jsonify({"status": True})

	def play_music(pathid):
    		my_sound = pygame.mixer.Sound(pathid)
    		my_sound.play()
 	 ```
- Next, we will modify the HTML page to include the audio controls.
	- In the body of the HTML page, include the following lines to add in controls for recording and sending audio.
  ```
    <div id="controls">
  	 <button id="recordButton">Record</button>
  	 <button id="pauseButton" disabled>Pause</button>
  	 <button id="stopButton" disabled>Stop</button>
    </div>
    <script src="https://cdn.rawgit.com/mattdiamond/Recorderjs/08e7abd9/dist/recorder.js"></script>
  	<script src="{{ url_for('static', filename='js/app.js') }}"></script>
  ```
- Now, our server has the ability to stream audio from the user to the Pi monitor!
- To make our page look nicer, we can include a CSS file. For this project, we used a modified version of the CSS file found in AddPipe's project. 
	- Save your CSS file in a folder called "css" within the "static" folder in the file structure.
	- Make sure your CSS file is called "style."	
## Sending Audio from the Pi Monitor to the Parent's Device
- To stream live audio from the Pi Monitor to the parent's device, we first have to create a header.
- The function below is included in "app.py". This function creates the header. The header contains important information about the audio data that we are transferring, such as the size, file type, etc.
    ```
	def genHeader(sampleRate, bitsPerSample, channels):
    		datasize = 2000*10**6
    		o = str('RIFF').encode('ascii')                                               # (4byte) Marks file as RIFF
    		o += to_bytes((datasize + 36),4,'little')                                     # (4byte) File size in bytes excluding this and RIFF marker
    		o += str('WAVE').encode('ascii')                                              # (4byte) File type
    		o += str("fmt ").encode('ascii')                                              # (4byte) Format Chunk Marker  
    		o += to_bytes(16,4,'little')                                                  # (4byte) Length of above format data 
    		o += to_bytes(1, 2, 'little')                                                 # (2byte) Format type (1 - PCM)
    		o += to_bytes(channels,2,'little')                                            # (2byte)
    		o += to_bytes(sampleRate,4,'little')                                          # (4byte)
    		o += to_bytes((sampleRate * channels * bitsPerSample // 8),4,'little')        # (4byte)
    		o += to_bytes((channels * bitsPerSample //8),2, 'little')                     # (2byte)
    		o += to_bytes(bitsPerSample, 2, 'little')                                     # (2byte)
    		o += str('data').encode('ascii')                                              # (4byte) Data Chunk Marker
    		o += to_bytes(datasize, 4, 'little')                                          # (4byte) Data size in bytes
    		return o

  ```
- After the header is created, we can start our audio stream using the 'audio' route. This route opens a stream from the Pi's USB microphone, attaches the generated header to the first chunk of the stream, and starts continously passing chunks of data to the server page for it to play as audio.
   ```
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

  ```
- Next, we must add code to the HTML file to display audio controls and allow for the parent to listen in on their baby.
- Add in the following lines. This will retrieve data from the 'audio' route, and allow the parent to hear their baby throughout the night!
   ```
    <audio controls>
        <source src="{{ url_for('audio') }}" type="audio/x-wav;codec=pcm">
        Your browser does not support the audio element.
    </audio>

  ```
## Future Work
- There are several great ideas that we did not have time to implement
	- Building a case to house the Pi, sonar, and camera would be a great addition to the project.
	- Adding in a temperature sensor that operates alongside the sonar.
	- Prerecorded sounds and melodies that could be played by the parent.

