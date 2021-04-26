# using opencv access webcam and transmit the video in HTML
import sys 
sys.path.append('/usr/local/lib/python3/site-packages')
import cv2 #opencv
import  pyshine as ps #  pip3 install pyshine==0.0.9
import serial

# ser = serial.Serial('/dev/ttyACM0')

HTML="""
<html>

<head>
    <title>Baby Monitor</title>
   
   <script type="text/javascript">
      let audioIN = { audio: true };
    //  audio is true, for recording
  
    // Access the permission for use
    // the microphone
    navigator.mediaDevices.getUserMedia(audioIN)
  
      // 'then()' method returns a Promise
      .then(function (mediaStreamObj) {
  
        // Connect the media stream to the
        // first audio element
        let audio = document.querySelector('audio');
        //returns the recorded audio via 'audio' tag
  
        // 'srcObject' is a property which 
        // takes the media object
        // This is supported in the newer browsers
        if ("srcObject" in audio) {
          audio.srcObject = mediaStreamObj;
        }
        else {   // Old version
          audio.src = window.URL
            .createObjectURL(mediaStreamObj);
        }
  
        // It will play the audio
        audio.onloadedmetadata = function (ev) {
  
          // Play the audio in the 2nd audio
          // element what is being recorded
          audio.play();
        };
  
        // Start record
        let start = document.getElementById('btnStart');
  
        // Stop record
        let stop = document.getElementById('btnStop');
  
        // 2nd audio tag for play the audio
        let playAudio = document.getElementById('adioPlay');
  
        // This is the main thing to recorde 
        // the audio 'MediaRecorder' API
        let mediaRecorder = new MediaRecorder(mediaStreamObj);
        // Pass the audio stream 
  
        // Start event
        start.addEventListener('click', function (ev) {
          mediaRecorder.start();
          // console.log(mediaRecorder.state);
        })
  
        // Stop event
        stop.addEventListener('click', function (ev) {
          mediaRecorder.stop();
          // console.log(mediaRecorder.state);
        });
  
        // If audio data available then push 
        // it to the chunk array
        mediaRecorder.ondataavailable = function (ev) {
          dataArray.push(ev.data);
        }
  
        // Chunk array to store the audio data 
        let dataArray = [];
  
        // Convert the audio data in to blob 
        // after stopping the recording
        mediaRecorder.onstop = function (ev) {
  
          // blob of type mp3
          let audioData = new Blob(dataArray, 
                    { 'type': 'audio/mp3;' });
            
          // After fill up the chunk 
          // array make it empty
          dataArray = [];
  
          // Creating audio url with reference 
          // of created blob named 'audioData'
          let audioSrc = window.URL
              .createObjectURL(audioData);
  
          // Pass the audio url to the 2nd video tag
          playAudio.src = audioSrc;
        }
      })
  
      // If any error occurs then handles the error 
      .catch(function (err) {
        console.log(err.name, err.message);
      });
   </script>
</head>

<body>
    <center><h1> Streaming Baby </h1></center>
    <center><img src="stream.mjpg" width='640' height='480' autoplay playsinline></center>
    
    
    <!--button for 'start recording'-->
    <p>
      <button id="btnStart">START RECORDING</button>
                
      <button id="btnStop">STOP RECORDING</button>
      <!--button for 'stop recording'-->
    </p>
  
    <!--for record-->
    <audio controls></audio>
    <!--'controls' use for add 
      play, pause, and volume-->
  
    <!--for play the audio-->
    <audio id="adioPlay" controls></audio>
    
</body>

</html>
"""
#<center><img src="stream.mjpg" width='640' height='480' autoplay playsinline></center>
#<h1>"data: " <span id="myText"></span></h1>
    
def main():
    StreamProps = ps.StreamProps
    StreamProps.set_Page(StreamProps,HTML)
    address = ('127.0.0.1',9000) # Enter your IP address 
    try:
        StreamProps.set_Mode(StreamProps,'cv2')
        capture = cv2.VideoCapture(0)
        capture.set(cv2.CAP_PROP_BUFFERSIZE,4)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH,320)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
        capture.set(cv2.CAP_PROP_FPS,30)
        StreamProps.set_Capture(StreamProps,capture)
        StreamProps.set_Quality(StreamProps,90)
        server = ps.Streamer(address,StreamProps)
        print('Server started at','http://'+address[0]+':'+str(address[1]))
        server.serve_forever()
        
    except KeyboardInterrupt:
        capture.release()
        server.socket.close()
        
if __name__=='__main__':
    main()
