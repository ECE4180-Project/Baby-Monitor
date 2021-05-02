# Baby Monitor
######  by Erobhosele Sado, Sidney Wise, Jack Darrow, and  Ben Nixon  

## Summary
A high-end baby monitor for worried parents. The monitor will stream a feed of the baby, check in on its movements, listen out for cries, and allow parents to speak to their child.

## Parts
- Raspberry Pi 3 
- Raspberry Pi NoIR Camera V2
- HC-SR04 Sonar Sensor
- USB Microphone
- Speaker 

# How It Works

## Setting up the hardware
- Connect the HC-SR04 Sonar Sensor to the Raspberry Pi 3
    - The HC-SR04 is powered using the Arduino Uno's 5V and GND pins, and operates using two GPIO pins. The two GPIO pins used in this process are GPIO pins 14 and 15.
    - The schematic below shows how to connect the HC-SR04 sensor using male to female dual head jumper wires.
- Connect the Raspberry Pi to a monitor or display. For this instance, the Pi was connected to a monitor using HDMI.
- Connect a USB keyboard and mouse to the Pi.
- Attach a speaker to the Pi through the 2.1mm headphone jack.
## Camera, Recorder & Server Setup 
To setup the camera first user must enable it on the Pi by going to **Preferences->Raspberry Pi Configuration-> Interfaces**
then reboot the Pi
Next download these modules in order to run the camera, recorder, and server
```
sudo apt-get install python3-flask
pip install -U -r requirements.txt
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365

```
To launch the server use this code
```
flask run
```
Once the server is running you can view the everything by going to ip:9000
```
http://000.000.0.0:8000
```
## Baby Motion trakcking

The baby's movement is tracked using the HC-SR04 Sonar Sensor

| Sonar  | Raspberry pi |
| ------------- | ------------- |
| Vcc  | 5V |
| Gnd | Gnd |
| trig | pin 17 |
| echo | pin 18  |

The sonar data is avreaged and has its standard deviation taken. 
If the distance is greater than the average plus two times the standard deviation or
less than the average minus two imes the standard deviation. 
The disrbance count is up signifying that the baby is moving.

## Speaking to the baby
Parents can talk to the baby thanks to the config file code in Microphone and SPeaker setup+connection.


## Video Demo
ggg

## Presentation
ggg
