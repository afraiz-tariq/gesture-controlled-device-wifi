# Hand Gesture Controlled LED over WiFi

This project demonstrates a system where hand gestures are recognized using a webcam and OpenCV, and the recognized gestures are used to control an LED connected to an ESP32-based microcontroller over WiFi.

## Table of Contents
- [Overview](#overview)
- [Components](#components)
- [Setup](#setup)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Troubleshooting](#troubleshooting)
- [Future Improvements](#future-improvements)

## Overview

The system uses a webcam to capture video, processes the video frames to recognize hand gestures using the MediaPipe library, and sends commands to an ESP32-based microcontroller over WiFi to control an LED. The gesture recognition is performed on a computer running Python, while the ESP32 hosts a simple web server to receive commands and control the LED.

## Components

- Computer with webcam
- ESP32-based microcontroller (Arduino Nano ESP32 or standard ESP32)
- LED
- Resistor (appropriate for your LED)
- Breadboard and jumper wires

## Setup

### Python Environment

1. Install the required Python libraries:
2. Update the `esp32_ip` variable in the Python script with the IP address of your ESP32-based device.

### ESP32 Setup

1. Install the Arduino IDE and set it up for ESP32 development.
- If using Arduino Nano ESP32, make sure to install the appropriate board package.
2. Open the Arduino sketch and update the WiFi credentials:
```cpp
const char* ssid = "Your_WiFi_SSID";
const char* pass = "Your_WiFi_Password";
Connect the LED to GPIO pin 5 of your ESP32-based device (don't forget to use an appropriate resistor).

Note: The pin number may vary depending on your specific board. Adjust if necessary.


Select the correct board in the Arduino IDE:

For Arduino Nano ESP32, select "Arduino Nano ESP32" from the boards menu.
For standard ESP32, select your specific ESP32 board model.


Upload the sketch to your ESP32-based device.

Usage

Run the Python script on your computer:
