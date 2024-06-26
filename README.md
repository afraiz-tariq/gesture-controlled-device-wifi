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
