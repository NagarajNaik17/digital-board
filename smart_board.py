import cv2
import mediapipe as mp
import numpy as np


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8
)
mp_drawing = mp.solutions.drawing_utils


canvas = None
smooth_points = []  
current_tool = 0  
colors = [(0, 0, 255), (255, 0, 0), (0, 0, 0), (255, 255, 255)]
brush_sizes = [7, 7, 7, 25]
prev_fingers = 0
buffer_size = 5 


cap = cv2.VideoCapture(0)
cv2.namedWindow('Smart Board', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('Smart Board', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

def get_smoothed_point(x, y):
    """Apply simple moving average to coordinates"""
    smooth_points.append((x, y))
    if len(smooth_points) > buffer_size:
        smooth_points.pop(0)
    return np.mean(smooth_points, axis=0, dtype=np.int32)

def count_fingers(landmarks):
    """Improved finger counting with threshold, including thumb"""
    count = 0
    threshold = 0.05  
    
    
    if landmarks[4].x < landmarks[3].x - threshold:  
        count += 1
   
    if landmarks[8].y < landmarks[6].y - threshold:
        count += 1
    
    if landmarks[12].y < landmarks[10].y - threshold:
        count += 1
   
    if landmarks[16].y < landmarks[14].y - threshold:
        count += 1
   
    if landmarks[20].y < landmarks[18].y - threshold:
        count += 1
    return count

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
   
    frame = cv2.flip(frame, 1)
    h, w = frame.shape[:2]
    if canvas is None:
        canvas = np.zeros((h, w, 3), dtype=np.uint8) + 255
    
   
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
       
        landmarks = hand_landmarks.landmark
        
      
        fingers = count_fingers(landmarks)
        
        
        cv2.putText(frame, f"Fingers: {fingers}", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        
       
        if fingers == 3 and prev_fingers != 3:
            current_tool = (current_tool + 1) % 4
            smooth_points.clear()  
       
        elif fingers == 5 and prev_fingers != 5:
            current_tool = 3  
            smooth_points.clear()
        
        elif fingers == 4 and prev_fingers != 4:
            brush_sizes[current_tool] += 2  
            smooth_points.clear()
     
        elif fingers == 2 and prev_fingers != 2:
            brush_sizes[current_tool] = max(2, brush_sizes[current_tool] - 2) 
            smooth_points.clear()
        
        prev_fingers = fingers
        
       
        x = int(landmarks[8].x * w)
        y = int(landmarks[8].y * h)
        
        
        x, y = get_smoothed_point(x, y)
        
        if fingers == 1:
            if len(smooth_points) >= 2:
                prev_point = smooth_points[-2]
                cv2.line(canvas, prev_point, (x, y), colors[current_tool], brush_sizes[current_tool])
            
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
        
       
        if fingers == 2:
            cv2.circle(frame, (x, y), brush_sizes[current_tool], colors[current_tool], 2)
            cv2.putText(frame, f"Size: {brush_sizes[current_tool]}", 
                       (x + 20, y + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[current_tool], 2)
    
    else:
        prev_fingers = 0
        smooth_points.clear()
    
   
    frame = cv2.addWeighted(frame, 0.4, canvas, 0.6, 0)
    
    
    cv2.rectangle(frame, (10, 10), (300, 60), (255, 255, 255), -1)
    cv2.putText(frame, f"Tool: {['Red Pen', 'Blue Pen', 'Black Pen', 'Eraser'][current_tool]}",
               (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, colors[current_tool], 2)
    
    cv2.imshow('Smart Board', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()