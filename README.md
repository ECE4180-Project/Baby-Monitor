# Baby-Monitor
######  by Erobhosele Sado, Sidney Wise, Jack Darrow, and  Ben Nixon                                                                                                     
A high-end baby monitor for worried parents. The monitor will stream a feed of the baby(using the pi camera), check in on its movements(using sonar sensors), listen out for cries(using microphone), and allow parents to speak to their child from another room(using the speaker).

## Parts
- Raspberry Pi 3 
- Mbed
- Raspberry Pi NoIR Camera V2
- HC-SR04 Sonar Sensor
- MEMS Microphone
- Speaker - PCB Mount

# How It Works
## Raspberry Pi 3
To setup the camera first user must enable it on the Pi by going to **Preferences->Raspberry Pi Configuration-> Interfaces**

Next download the opencv in order to run the camera
```
sudo apt-get install libhdf5-dev libhdf5-serial-dev
sudo apt-get install python3-h5py
sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install -y libatlas-base-dev libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqtgui4 libqt4-test
sudo pip3 install opencv-contrib-python==3.4.4.19
```
To run the camera and launch the server use this code
```
python3 main.py
```
Once the server is running you can view the everything by going to ip:9000
```
http://111.111.1.1:9000
```


## Mbed
words
| Mbed  | part |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
