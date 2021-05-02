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

## How it Works

### Sonar Detection
- The baby's movement is tracked using the HC-SR04 Sonar Sensor

| Sonar  | Raspberry pi |
| ------------- | ------------- |
| Vcc  | 5V |
| Gnd | Gnd |
| trig | pin 14 |
| echo | pin 15  |

- For the Pi to operate the sonar, a custom class called "sonar" was made. This class takes in an integer number for the sonar's trigger pin, an integer number for the sonar's echo pin, and if desired, a long integer number that represents the desired timeout delay for the sonar.
- Within the class is a function called "distance." the distance function will return the distance in millimeters from the sonar to an object.

## Speaking to the baby
Parents can talk to the baby thanks to the config file code in Microphone and SPeaker setup+connection.


## Video Demo
ggg

## Presentation
ggg
