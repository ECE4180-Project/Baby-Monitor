# Baby Monitor
######  by Erobhosele Sado, Sidney Wise, Jack Darrow, and  Ben Nixon  

## Summary
A high-end baby monitor for worried parents. The monitor will stream a feed of the baby, check in on its movements, listen out for cries, and allow parents to speak to their child.

## Parts
- Raspberry Pi 3 
- MicroUSB cable
- Monitor or display with appropriate cables to connect to the Pi
- Raspberry Pi NoIR Camera V2
- HC-SR04 Sonar Sensor
- USB Microphone
- Speaker with 2.1mm jack input 

# How It Works

## Setting Up the Hardware
- Connect the HC-SR04 Sonar Sensor to the Raspberry Pi 3
    - The HC-SR04 is powered using the Arduino Uno's 5V and GND pins, and operates using two GPIO pins. The two GPIO pins used in this process are GPIO pins 14 and 15.
    - The schematic below shows how to connect the HC-SR04 sensor using male to female dual head jumper wires.
- Connect the Raspberry Pi to a monitor or display. For this instance, the Pi was connected to a monitor using HDMI.
- Plug the USB microphone into the Pi.
- Connect a USB keyboard and mouse to the Pi.
- Attach a speaker to the Pi through the 2.1mm headphone jack.

## Camera, Recorder & Server Setup 
- To setup the camera first user must enable it on the Pi by going to **Preferences->Raspberry Pi Configuration-> Interfaces**, then reboot the Pi
- Next, download these modules in order to run the camera, recorder, and server.
```
sudo apt-get install python3-flask
sudo apt-get install pydub
sudo apt-get install pyaudio

```
- After installation is complete, generate a Secure Socket Layer (SSL). Type in the line below, and follow the instructions.
```
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout -key.pem -days 365
```
- When the Secure Sockets Layer is generated, run the server using the command below.
```
flask run --cert=cert.pem --key=key.pem
```
- Copy and paste the generated hyperlink into your web browser, and watch your baby in real time!


## Sonar Detection
<p align="center">
  <img src="https://user-images.githubusercontent.com/82454615/116896397-34c26800-ac02-11eb-8a26-f865a4ca29db.png" width=30% height=30% >
</p>
<p align="center">
  HCSR04 from Sparkfun
</p>
- The baby's movement is tracked using the HC-SR04 Sonar Sensor
- The sonar operates by sending out a pulse and then measuring how long it takes for the entire pulse to bounce off an object an return to the sensor.
- The time it takes for the pulse to bounce off an object and return is dependent upon how far away the object is.
<p align="center>
  <img src="https://static.javatpoint.com/tutorial/arduino/images/arduino-ultrasonic-distance-sensor4.png" width=30% height=30% >
</p>




| Sonar  | Raspberry pi |
| ------------- | ------------- |
| Vcc  | 5V |
| Gnd | Gnd |
| trig | pin 14 |
| echo | pin 15  |

- For the Pi to operate the sonar, a custom class called "sonar" was made that utilizes the PIGPIO library (http://abyz.me.uk/rpi/pigpio/). This class takes in an integer number for the sonar's trigger pin, an integer number for the sonar's echo pin, and if desired, a long integer number that represents the desired timeout delay for the sonar.
- Within the class is a function called "distance." the distance function will return the distance from the sonar to an object.
    - The distance function starts by storing the current number of microseconds since system boot in the "trackTick" variable.

    - Next, the PIGPIO library is used to set the GPIO level on the trigger pin to LOW for two microseconds. Then, the GPIO level on the trigger pin is set high for 10 microseconds, and then set LOW again. This creates the ultrasonic pulse.
    - The receiver portion of the HC-SR04 then waits for the ultrasonic pulse to bounce back. When the sensor detects the beginning of the waveform returning to the sensor, the PIGPIO libary will read a high value on the echo pin, and the program will mark the current time in microseconds since system boot.
    - After the entire waveform has returned to the sonar, the PIGPIO library will read a low value on the echo pin, and the program will once again mark the time since system boot. 
    - The difference in time since system boot at the start of the waveform and at the end of the waveform is found. 
    - This time difference decreases as an object gets closer to the sonar and increases as an object gets farther away from the sonar.
```// Function to figure out the distance
int sonar::distance()
{
  
  // Variable used to measure start time of high echo pin value
  uint32_t startTick = 0;
  uint32_t trackTick = 0;
  // Variable used to measure end time of high echo pin value
  uint32_t endTick = 0;
  // Variable used to store the time difference between startTick and endTick.
  int diffTick = 0;
  // GPIO tick used for timout purposes.
  trackTick = gpioTick();
  // Set the trigger pin low for 2 microseconds, high for 10 microseconds, and then low again.
  gpioWrite(triggergpio, PI_OFF);
  gpioDelay(2);
  gpioWrite(triggergpio, PI_ON);
  gpioDelay(10);
  gpioWrite(triggergpio, PI_OFF);
  // Continuously set startTick to the current tick until the echo pin goes high (receive signal) or time expires.
  while(gpioRead(echogpio) == 0 && (gpioTick() < (trackTick + timeout))){
	  startTick = gpioTick();
  }
  // Continuously update set endTick to the current tick while the echo pin is high.
  while(gpioRead(echogpio) == 1){
	 endTick = gpioTick();
  }
  // the startTick value now represents the time at which the sonar started receiving the echo back.
  // the endTick value represents the time at which the sonar stopped receiving the echo back.
  // diffTick is the time between the start of receiving the wave back and the end of receiving the wave back.
  diffTick = endTick - startTick;
  if(diffTick > timeout){
      diffTick = timeout;
  }
  return ((int) diffTick);
}
```
## Creating a Disturbance Metric
- To create a metric that effectively communicates how active the baby is, some basic statistics are used to analyze data from the sonar.
- The program "FilterVersion.cpp" both obtains and analyzes the sonar data using a continous loop that executes once every 0.25 seconds.
- The the main function of the program starts by initilizing the PIGPIO library, creating a length 100 data array to continuously store the latest sonar data, and initializing all the values in this array to 0.
- The program then enters a "while" loops that runs indefinitely. 
- The loop starts by shifting all data array values down by one place to make room for the newest data value.
- An instance of the sonar class is used to determine the current distance the baby is from the sensor. This new data value is then added to the data array.
- The average value of the length 100 data array is calculated. This average value is used along with the 100 data values to calculate the current standard deviation of the 100 distance data values.
- Next, the current distance value is analyzed. if the current distance is greater than the current mean plus two times the standard deviation, or less than the mean minus two times the standard deviation, a disturbance count variable is incremented by one.
- This disturbance count value is then written to the standard output stream, and the data measurement and analysis process starts again.
- This process is completed once every 0.25 seconds indefinitely.
- In order to prevent the initial startup of the sensor from generating false disturbances, there is logic in place to prevent the disturbance count value from being incremented until 125 measurements have been taken.
## Speaking to the baby
Parents can talk to the baby thanks to the config file code in Microphone and SPeaker setup+connection.


## Video Demo
ggg

## Presentation
ggg
