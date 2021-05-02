#include <stdio.h>
#include <signal.h>
#include <pigpio.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>
#include <math.h>
#include <iostream>

//using namespace std;
// Class developed to use the HC-SR04 ultrasonic sonar sensor.
class sonar{
	public:
  
  // GPIO pin connected to the "Trig" pin on the sonar.
	int triggergpio;
  
  // GPIO pin connected to the "Echo" pin on the sonar.
	int echogpio;
  
  // Time out duration in microeconds.
	long timeout;
  
  // Function to read in time for an instance of the class.
	int distance();
  
  // Constructor with default timeout of 3000usec.
	sonar(int Trigger, int Echo);
  
  // Constructor that allows custom timeout.
	sonar(int Trigger, int Echo, long timeout_val);
  
  // Destructor
  //~sonar();
	
};

// Constructor with default tmiout setting
sonar::sonar(int Trigger, int Echo)
{
   // Set the GPIO pin connected to the sonar trigger to output.
   gpioSetMode(Trigger, PI_OUTPUT);
   
   // Set the GPIo pin connected to the sonar echo to input.
   gpioSetMode(Echo,PI_INPUT);
   
   // Store the trigger pin number in the triggergpio variable.
   triggergpio= Trigger;
   
   // Store the echo pin number in teh echogpio variable.
   echogpio = Echo;
   
   // Assign timeout value of 3000us.
   timeout=3000; 
}

// Constructor with custom timeout setting
sonar::sonar(int Trigger, int Echo, long timeout_val)
{
   // Set the GPIO pin connected to the sonar trigger to output.
   gpioSetMode(Trigger,PI_OUTPUT);
   
   // Set the GPIo pin connected to the sonar echo to input.
   gpioSetMode(Echo,PI_INPUT);
   
   // Store the trigger pin number in the triggergpio variable.
   triggergpio=Trigger;
   
   // Store the echo pin number in teh echogpio variable.
   echogpio=Echo;
   
   // Store the custom timeout value in the timeout variable.
   timeout=timeout_val;
}

// Function to figure out the distance
int sonar::distance()
{
  
  // Variable used to measure start time of high echo pin value
  uint32_t startTick = 0;
  
  // 
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




int main(int argc, char *argv[])
{
  //gpioTerminate();
  
  if (gpioInitialise()<0) return 1;
  
  // Variable to keep track of the number of disturbances
  int disturbance_count = 0;
  
  // Variable that sets the length of the running data array
  int len = 100;
  
  // Variable that stores the standard deviation for each iteration
  int std_dev = 0;
  
  // Variable that stores the average for each iteration
  int average = 0;
  
  // Array to store data from the sonar.
  int data_arr [len];
  
  // Variable used ot determine when to start reporting disturbances.
  int gate = 0;
  
  // Initialize data array to zero.
  for(int i = 0; i <= (len - 1); i = i +1){
    data_arr[i] = 0;
  }  
  
  // Set up the sonar that will be used to retrieve data points
  sonar sonar1(15,14);


   while (1){
      // the array "data_arr" stores the data points taken from the sonar.
      // Data points from sonar are all shifted down by one place inside the data array.
      for(int i = 0; i <= (len - 2); i = i + 1){
        data_arr[i] = data_arr [i + 1];
      }
      
      // A new data point is added to the data array.
        data_arr[(len - 1)] = sonar1.distance();
      
      // The average value of all the data currently in the array is calculated.
      average = 0;
      for(int i = 0; i <= (len - 1); i = i + 1){
          average = average + data_arr[i];
      }
      average = average / len;
      
    
      // The standard deviation for this iteration of the data array is calculated.
      std_dev = 0;
      for(int i = 0; i <= (len - 1); i = i + 1){
        std_dev = std_dev + ((data_arr[i] - average)*(data_arr[i] - average));
      }
      std_dev = std_dev / len;
      std_dev = sqrt(std_dev);
    
   
      // If the newest data point in the data array is greater than the average plus two times the standard deviation
      // or less than the average minus two imes the standard deviation, the disturbance count is incremented.
      if(((data_arr[(len - 1)] > (average + 2 * std_dev)) || (data_arr[(len - 1)] < (average - 2 * std_dev))) && std_dev > 15){
        if(gate >= (len + 25)){
          disturbance_count = disturbance_count + 1;
        }
      }
      if(gate < (len + 25)){
        gate = gate + 1;
      }
      
      
      
    // printf( "%s %u %s %u %s %u %s %u \n", "Standard Deviation  ",std_dev, "  Average  ", average, "  Disturbance Count  ", disturbance_count, "  New Value  ",data_arr[(len - 1)]) ; /// sonar1.Timing()"%u\n", 
      
      std::cout << data_arr[(len - 1)] << std::endl;
      std::cout.flush();
      
      time_sleep(0.25);
      
   }
   gpioTerminate();

   return 0;
} 

