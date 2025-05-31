
---

## 🔍 Overview

This project captures live video from your webcam, converts each frame to HSV color space, applies a threshold for “yellow” pixels, finds contours for every connected yellow region, and then:

1. Filters out small contours (noise) by area.
2. Draws a green bounding box around each detected yellow object.
3. Labels each bounding box with a count index (1, 2, 3, …).
4. Displays the current FPS in the top-left.

---

## ⚙️ Installation

1. **Clone or download** this folder onto your machine.
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate       # On Windows use `venv\Scripts\activate`
