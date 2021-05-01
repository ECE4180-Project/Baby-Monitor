# Baby Monitor
######  by Erobhosele Sado, Sidney Wise, Jack Darrow, and  Ben Nixon  

## Summary
A high-end baby monitor for worried parents. The monitor will stream a feed of the baby, check in on its movements, listen out for cries, and allow parents to speak to their child.

## Parts
- Raspberry Pi 3 
- Mbed
- Raspberry Pi NoIR Camera V2
- HC-SR04 Sonar Sensor
- MEMS Microphone
- Speaker - PCB Mount

# How It Works
## Camera & Server Setup 
To setup the camera first user must enable it on the Pi by going to **Preferences->Raspberry Pi Configuration-> Interfaces**
then reboot the Pi
Next download these modules in order to run the camera and server
```
pip install flask
pip install numpy
pip install opencv-contrib-python
pip install imutils

```
To launch the server use this code
```
python webstreaming.py --ip 0.0.0.0 --port 8000
```
Once the server is running you can view the everything by going to ip:9000
```
http://0.0.0.0:8000
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
