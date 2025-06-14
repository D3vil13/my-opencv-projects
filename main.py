import os
import cv2
import numpy as np
import time
import mediapipe as mp
import handtrackmodule as htm 
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

#volume control for windows
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices. Activate(
IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER (IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
# print("Volume Range:", volume.GetVolumeRange())
minVol = volRange[0]
maxVol = volRange[1]    



vol = 0
volBar = 400
volPer = 0
wcam = 1280
hcam = 720

ctime = 0
ptime = 0

cap = cv2.VideoCapture(1)
cap.set(3, wcam)  # Set width
cap.set(4, hcam)  # Set height


detector = htm.HandDetector(detectionCon=0.7)

while True:
    
    ret, frame = cap.read()
    
    frame = detector.findHands(frame)
    lmlist = detector.findPosition(frame, draw=False)
    if len(lmlist) != 0:
        # print(lmlist[4], lmlist[8])
        
        x1, y1 = lmlist[4][1], lmlist[4][2]  # Thumb tip
        x2, y2 = lmlist[8][1], lmlist[8][2] # Index finger tip
        cv2.circle(frame, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(frame, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        cv2.circle(frame, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)
        # print(length)
        
        # Hand range 50 - 300
        # Volume range -63.5 to 0.0
        
        # Clamp to valid range
        clamped_length = np.clip(length, 40, 260)
        # Scale to log space: map [40, 260] to [1, 100]
        scaled_length = np.interp(clamped_length, [40, 260], [1, 100])

        # Apply logarithmic scaling
        log_scaled = math.log10(scaled_length) / math.log10(100)  # in [0, 1]
        vol = minVol + (maxVol - minVol) * log_scaled

        volBar = np.interp(length, [40, 260], [400, 150])
        volPer = np.interp(length, [40, 260], [0, 100])
        print(length, vol)
        volume. SetMasterVolumeLevel(vol, None)
        
        if length < 50:
            cv2.circle(frame, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
        
  
     
    cv2.rectangle(frame, (50, 150), (85, 400), (0, 255, 0), 3)
    cv2.rectangle(frame, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(frame, f'Volume: {int(volPer)}%', (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
       
    
cap.release()    
cv2.destroyAllWindows()