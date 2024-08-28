import serial
import cv2
import dlib

# Initialize serial port
ser = serial.Serial("/dev/serial0", 115200)

# Function to get TFmini distance
def get_distance():
    count = ser.in_waiting
    if count > 8:
        recv = ser.read(9)
        ser.reset_input_buffer()
        if recv[0] == 89 and recv[1] == 89:  # Use decimal values instead of hex
            low = int(recv[2])
            high = int(recv[3])
            distance = low + high * 256
            return distance
    return None

# Initialize dlib's face detector and facial landmarks predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Function to detect face landmarks using dlib
def detect_face_landmarks(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)
    landmarks = []
    for rect in rects:
        shape = predictor(gray, rect)
        for i in range(68):
            landmarks.append((shape.part(i).x, shape.part(i).y))
    return landmarks

if __name__ == '__main__':
    try:
        # Open serial port
        if not ser.is_open:
            ser.open()

        # Get TFmini distance once
        distance = get_distance()
        print("Initial distance:", distance)

        # Open webcam
        cap = cv2.VideoCapture(0)

        while cap.isOpened():
            # Read frame from webcam
            ret, frame = cap.read()
            if not ret:
                break

            # Detect face landmarks
            landmarks = detect_face_landmarks(frame)
            
            # Draw face landmarks on the frame
            for landmark in landmarks:
                cv2.circle(frame, landmark, 1, (0, 255, 0), -1)

            # Display the frame
            cv2.imshow('Frame', frame)

            # Check for 'q' key to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release resources
        cap.release()
        cv2.destroyAllWindows()

    except KeyboardInterrupt:   # Ctrl+C
        if ser is not None:
            ser.close()
