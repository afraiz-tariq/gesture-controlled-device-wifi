**Hand Gesture Controlled LED over WiFi**



This project demonstrates a system where hand gestures are recognized using a webcam and OpenCV, and the recognized gestures are used to control an LED connected to an ESP32-based microcontroller over WiFi.



**Table of Contents**


Overview
Components
Setup
Usage
Code Explanation
Troubleshooting
Future Improvements



**Overview**


The system uses a webcam to capture video, processes the video frames to recognize hand gestures using the MediaPipe library, and sends commands to an ESP32-based microcontroller over WiFi to control an LED. The gesture recognition is performed on a computer running Python, while the ESP32 hosts a simple web server to receive commands and control the LED.



**Components**


Computer with webcam
ESP32-based microcontroller (Arduino Nano ESP32 or standard ESP32)
LED
Resistor (appropriate for your LED)
Breadboard and jumper wires



**Setup**


Python Environment

Install the required Python libraries:
Copypip install opencv-python mediapipe requests

Update the esp32_ip variable in the Python script with the IP address of your ESP32-based device.



**ESP32 Setup**


Install the Arduino IDE and set it up for ESP32 development.

If using Arduino Nano ESP32, make sure to install the appropriate board package.


Open the Arduino sketch and update the WiFi credentials:
cppCopyconst char* ssid = "Your_WiFi_SSID";
const char* pass = "Your_WiFi_Password";

Connect the LED to GPIO pin 5 of your ESP32-based device (don't forget to use an appropriate resistor).

Note: The pin number may vary depending on your specific board. Adjust if necessary.


Select the correct board in the Arduino IDE:

For Arduino Nano ESP32, select "Arduino Nano ESP32" from the boards menu.
For standard ESP32, select your specific ESP32 board model.


Upload the sketch to your ESP32-based device.



**Usage**


Run the Python script on your computer:
Copypython hand_gesture_control.py

The webcam feed will open, showing the recognized hand landmarks.
Make hand gestures in front of the camera:

Open hand (all fingers extended): Turns the LED on
Closed hand (fist): Turns the LED off





**Code Explanation**


**Python Script**


The Python script (hand_gesture_control.py) does the following:

Initializes the webcam and MediaPipe Hands module.
Captures video frames and processes them to detect hand landmarks.
Recognizes gestures based on the positions of fingertips relative to their interphalangeal joints.
Sends HTTP requests to the ESP32-based device to control the LED based on the recognized gesture.
Displays the processed video feed with hand landmarks and gesture information.



**Arduino Sketch**


The Arduino sketch running on the ESP32-based device (Arduino Nano ESP32 or standard ESP32) does the following:

Connects to the specified WiFi network.
Sets up a web server.
Listens for incoming HTTP requests.
Controls the LED based on the received commands ("/H" for on, "/L" for off).



**Troubleshooting**


If the Python script can't connect to the ESP32-based device, make sure both devices are on the same WiFi network and the IP address is correct.
If gestures are not being recognized properly, try adjusting lighting conditions or the min_detection_confidence and min_tracking_confidence parameters in the Python script.
If using the Arduino Nano ESP32 and encountering issues, ensure you have the latest board package installed and selected the correct board in the Arduino IDE.
