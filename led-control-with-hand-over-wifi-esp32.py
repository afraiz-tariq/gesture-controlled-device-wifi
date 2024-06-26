import cv2
import mediapipe as mp
from threading import Thread, Event
import queue
import requests  # Required for sending HTTP requests

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    model_complexity=0,  # Use simpler model for faster processing
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    max_num_hands=1,
)
mp_drawing = mp.solutions.drawing_utils

# ESP32 server information
esp32_ip = '192.168.219.103'  # Replace with the actual IP address of your ESP32
led_on_url = f"http://{esp32_ip}/H"
led_off_url = f"http://{esp32_ip}/L"

# Function to recognize hand gestures
def recognize_gesture(hand_landmarks):
    fingertips = [
        hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP],
        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP],
        hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
        hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP],
        hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
    ]
    finger_ips = [
        hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP],
        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP],
        hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP],
        hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP],
        hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP]
    ]

    # Gesture recognition based on the position of fingertips relative to interphalangeal joints
    if all(fingertip.y < ip.y for fingertip, ip in zip(fingertips, finger_ips)):
        return "Hand Open", '1'
    return "Hand Closed", '0'

# Function to send commands to ESP32 over WiFi
def control_led(command):
    url = led_on_url if command == '1' else led_off_url
    try:
        requests.get(url)  # Send the HTTP request
    except requests.exceptions.RequestException as e:
        print(f"Failed to send command to ESP32: {e}")

# Function to capture frames from the webcam
def capture_frames(cap, frame_queue, stop_event):
    while not stop_event.is_set():
        ret, frame = cap.read()
        if not ret:
            stop_event.set()
        frame = cv2.resize(frame, (640, 480))  # Resize for consistent processing
        frame_queue.put(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            stop_event.set()

# Function to process frames for hand gesture recognition
def process_frames(frame_queue, stop_event):
    while not stop_event.is_set() or not frame_queue.empty():
        if not frame_queue.empty():
            frame = frame_queue.get()
            frame = cv2.flip(frame, 1)  # Mirror the frame
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
            result = hands.process(rgb_frame)  # Process the frame through MediaPipe

            gesture, command = "No hand detected", '0'
            if result.multi_hand_landmarks:
                for hand_landmarks in result.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    gesture, command = recognize_gesture(hand_landmarks)
                    control_led(command)  # Control LED based on gesture

            cv2.putText(frame, gesture, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.imshow('Hand Gesture Recognition', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                stop_event.set()

# Main function to setup and run the application
def main():
    cap = cv2.VideoCapture(0)  # Start video capture
    frame_queue = queue.Queue(maxsize=5)
    stop_event = Event()

    # Create and start threads for capturing and processing frames
    capture_thread = Thread(target=capture_frames, args=(cap, frame_queue, stop_event))
    process_thread = Thread(target=process_frames, args=(frame_queue, stop_event))

    capture_thread.start()
    process_thread.start()

    capture_thread.join()
    process_thread.join()

    cap.release()  # Release the video capture object
    cv2.destroyAllWindows()  # Close all OpenCV windows
    hands.close()  # Close MediaPipe Hands

if __name__ == "__main__":
    main()
