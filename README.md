**Hand Gesture Controlled LED over WiFi**
This project demonstrates a system where hand gestures are recognized using a webcam and OpenCV, and the recognized gestures are used to control an LED connected to an ESP32-based microcontroller over WiFi.
Table of Contents
•	Overview
•	Components
•	Setup
•	Usage
•	Code Explanation
•	Troubleshooting
•	Future Improvements
Overview
The system uses a webcam to capture video, processes the video frames to recognize hand gestures using the MediaPipe library, and sends commands to an ESP32-based microcontroller over WiFi to control an LED. The gesture recognition is performed on a computer running Python, while the ESP32 hosts a simple web server to receive commands and control the LED.
Components
•	Computer with webcam
•	ESP32-based microcontroller (Arduino Nano ESP32 or standard ESP32)
•	LED
•	Resistor (appropriate for your LED)
•	Breadboard and jumper wires
Setup
Python Environment
1.	Install the required Python libraries: 
Copy
pip install opencv-python mediapipe requests
2.	Update the esp32_ip variable in the Python script with the IP address of your ESP32-based device.
ESP32 Setup
1.	Install the Arduino IDE and set it up for ESP32 development. 
o	If using Arduino Nano ESP32, make sure to install the appropriate board package.
2.	Open the Arduino sketch and update the WiFi credentials: 
cpp
Copy
const char* ssid = "Your_WiFi_SSID";
const char* pass = "Your_WiFi_Password";
3.	Connect the LED to GPIO pin 5 of your ESP32-based device (don't forget to use an appropriate resistor). 
o	Note: The pin number may vary depending on your specific board. Adjust if necessary.
4.	Select the correct board in the Arduino IDE: 
o	For Arduino Nano ESP32, select "Arduino Nano ESP32" from the boards menu.
o	For standard ESP32, select your specific ESP32 board model.
5.	Upload the sketch to your ESP32-based device.
Usage
1.	Run the Python script on your computer: 
Copy
python hand_gesture_control.py
2.	The webcam feed will open, showing the recognized hand landmarks.
3.	Make hand gestures in front of the camera: 
o	Open hand (all fingers extended): Turns the LED on
o	Closed hand (fist): Turns the LED off
Code Explanation
Python Script
The Python script (hand_gesture_control.py) does the following:
1.	Initializes the webcam and MediaPipe Hands module.
2.	Captures video frames and processes them to detect hand landmarks.
3.	Recognizes gestures based on the positions of fingertips relative to their interphalangeal joints.
4.	Sends HTTP requests to the ESP32-based device to control the LED based on the recognized gesture.
5.	Displays the processed video feed with hand landmarks and gesture information.
Arduino Sketch
The Arduino sketch running on the ESP32-based device (Arduino Nano ESP32 or standard ESP32) does the following:
1.	Connects to the specified WiFi network.
2.	Sets up a web server.
3.	Listens for incoming HTTP requests.
4.	Controls the LED based on the received commands ("/H" for on, "/L" for off).
Troubleshooting
•	If the Python script can't connect to the ESP32-based device, make sure both devices are on the same WiFi network and the IP address is correct.
•	If gestures are not being recognized properly, try adjusting lighting conditions or the min_detection_confidence and min_tracking_confidence parameters in the Python script.
•	If using the Arduino Nano ESP32 and encountering issues, ensure you have the latest board package installed and selected the correct board in the Arduino IDE.

