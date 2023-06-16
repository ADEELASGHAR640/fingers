import cv2
import mediapipe as mp

# Create an empty array to store the values
finger_status = [0, 0, 0, 0, 0]

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.8)

# Initialize OpenCV capture
cap = cv2.VideoCapture(0)

while True:
    # Read frame from video capture
    ret, frame = cap.read()

    # Convert frame to RGB for processing with MediaPipe Hands
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image with MediaPipe Hands
    results = mp_hands.process(image_rgb)

    #print(results.multi_hand_landmarks )


    # Check hand landmarks and perform actions
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
                cv2.putText(frame, "Thumb open", (int(hand_landmarks.landmark[4].x * frame.shape[1]), int(hand_landmarks.landmark[4].y * frame.shape[0])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                finger_status[0] = 1
            else:
                finger_status[0] = 0
            if hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y:
                cv2.putText(frame, "Index open", (int(hand_landmarks.landmark[8].x * frame.shape[1]), int(hand_landmarks.landmark[8].y * frame.shape[0])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                finger_status[1] = 1
            else:
                finger_status[1] = 0
            if hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y:
                cv2.putText(frame, "Middle open", (int(hand_landmarks.landmark[12].x * frame.shape[1]), int(hand_landmarks.landmark[12].y * frame.shape[0]-20)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                finger_status[2] = 1
            else:
                finger_status[2] = 0
            
            if hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y:
                cv2.putText(frame, "Ring open", (int(hand_landmarks.landmark[16].x * frame.shape[1]-40), int(hand_landmarks.landmark[16].y * frame.shape[0]-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                finger_status[3] = 1
            else:
                finger_status[3] = 0
            if hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y:
                cv2.putText(frame, "pinky open", (int(hand_landmarks.landmark[20].x * frame.shape[1]-80), int(hand_landmarks.landmark[20].y * frame.shape[0])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                finger_status[4] = 1
            else:
                finger_status[4] = 0
            
            # print(finger_status)
            # print(sum(finger_status))
            total_fingers=sum(finger_status)

            cv2.putText(frame,"Total Fingers open: " + str(total_fingers), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)

        
            # else:
                # cv2.putText(frame, "Closed", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                # finger_status.append(0)
                # print(finger_status)
            # Draw hand landmarks on the frame
            for landmark in hand_landmarks.landmark:
                x = int(landmark.x * frame.shape[1])
                y = int(landmark.y * frame.shape[0])
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
        
        print(finger_status)

    # Display the output frame
    cv2.imshow('Hand Tracking', frame)

    # Exit loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy windows
cap.release()
cv2.destroyAllWindows()