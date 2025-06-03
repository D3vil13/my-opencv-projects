import cv2
import mediapipe as mp


def process_img(img,face_detection):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    if out.detections is not None:
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box
            x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

            x1 = int(x1 * W)
            y1 = int(y1 * H)
            w = int(w * W)
            h = int(h * H)

            # Blur the detected face region
            img[y1:y1 + h, x1:x1 + w, :] = cv2.blur(img[y1:y1 + h, x1:x1 + w, :], (30, 30), 0)

    return img



#detech image
mp_face_detection = mp.solutions.face_detection
with mp_face_detection.FaceDetection(min_detection_confidence=0.2,model_selection=0) as face_detection:
    
    

        cap = cv2.VideoCapture(0)
        
        ret , frame = cap.read()
        H, W, C = frame.shape
        frame = process_img(frame, face_detection)
        while ret:
            frame = process_img(frame, face_detection)
            cv2.imshow("Blurred Video", frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            ret , frame = cap.read()
        cap.release()
        cv2.destroyAllWindows()
    
    




