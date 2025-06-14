# Hand Gesture Volume Controller (Logarithmic Scaling)

This is the fifth project in my 30-day Computer Vision challenge.

The application uses your webcam to detect hand gestures (thumb and index finger distance) to control your system volume. The volume scaling is implemented using a **logarithmic mapping** for more natural audio perception.

---

## 🔧 Features

- Real-time webcam feed
- Hand landmark detection using MediaPipe
- Distance between thumb and index finger controls volume
- Logarithmic scaling of volume to better match human hearing
- Visual feedback with FPS and volume bar

---

## 📦 Requirements

Install the required libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
