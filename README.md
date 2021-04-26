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
## Camera and audio Setup 
Both the caream and audio is run through the a wbesever streamed to the parents
To setup the camera first user must enable it on the Pi by going to **Preferences->Raspberry Pi Configuration-> Interfaces**
then reboot the Pi
Next download the opencv in order to run the camera
```
sudo apt-get install libhdf5-dev libhdf5-serial-dev
sudo apt-get install python3-h5py
sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install -y libatlas-base-dev libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqtgui4 libqt4-test
sudo pip3 install opencv-contrib-python==3.4.4.19
pip3 install pyshine==0.0.9
```
To run the camera, audio and launch the server use this code
```
python3 camera.py
```
Once the server is running you can view the everything by going to ip:9000
```
http://111.111.1.1:9000
```
## Baby Motion trakcking

The baby's movement is tracked using the HC-SR04 Sonar Sensor

| Sonar  | Raspberry pi |
| ------------- | ------------- |
| Vcc  | 5V |
| Gnd | Gnd |
| trig | pin 17 |
| echo | pin 18  |

Once connected the *place description for sonar*

## Video Demo
ggg

## Presentation
ggg
