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

Then in the terminal type in:
```
sudo apt-get update
sudo apt-get upgrade
sudo apt install apache2 -y
cd /var/www/html 
ls -al 
sudo chown pi: index.html
sudo nano index.html
```
Once in the file copy paste in the camera code in the pi file
to get to webpage
```
sudo service apache2 status
```

## Mbed
words
| Mbed  | part |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
