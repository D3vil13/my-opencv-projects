import cv2
from utils import get_limits
import time

yellow = (0, 255, 255)  # BGR color for yellow (will be converted to HSV bounds via get_limits)
ctime = 0
ptime = 0

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # ----- FPS calculation (unchanged) -----
    ctime = time.time()
    fps = 1 / (ctime - ptime) if (ctime - ptime) > 0 else 0
    ptime = ctime
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Convert to HSV and threshold on yellow
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(yellow)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # ----- Find contours on the binary mask -----
    
    contours, hierarchy = cv2.findContours(
        mask, 
        cv2.RETR_EXTERNAL,      # only external contours
        cv2.CHAIN_APPROX_SIMPLE # compresses horizontal, vertical, and diagonal segments
    )

    # Loop over each contour and draw a bbox around it
    count =  0
    for cnt in contours:
        
        area = cv2.contourArea(cnt)
        # Optional: skip tiny contours (tune this threshold as needed)
        if area < 350:
            continue

        x, y, w, h = cv2.boundingRect(cnt)
        count += 1
        cv2.putText(frame, f'{count}' , (x-1, y-1),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the result
    cv2.imshow('frame', frame)

    # Press 'q' to break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
