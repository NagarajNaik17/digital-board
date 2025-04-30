


# 🖐️ Digital Board

A virtual whiteboard powered by **OpenCV** and **MediaPipe**, enabling users to draw on screen using only hand gestures via a webcam. Perfect for presentations, teaching, or fun interactive demos — no mouse or stylus needed!

---

## ✨ Features

- 👆 Hand gesture-controlled drawing
- 🖍️ Multiple tools: Red, Blue, Black pens & Eraser
- 📏 Adjustable brush sizes via gesture
- 🔄 Tool switching with intuitive finger gestures
- 🧠 Smoothed drawing using a moving average filter
- 🖥️ Full-screen drawing experience

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/NagarajNaik17/digital-board.git
cd digital-board
```

### 2. Install Dependencies

Make sure you have Python 3.7+ installed.

```bash
pip install opencv-python mediapipe numpy
```

### 3. Run the Application

```bash
python smart_board.py
```



---

## 🧠 Gesture Controls

| Gesture            | Action                       |
|--------------------|------------------------------|
| 1 finger (index)   | Draw                         |
| 3 fingers          | Switch tool (cycle pens/eraser) |
| 5 fingers          | Increase brush size           |
| 4 fingers          | Descrease brush size          |
| 2 fingers          | change position without writing          |

---

## 🖥️ Project Structure

```
digital-board/
│
├── main.py          # Main application code
├── README.md        # This file
└── requirements.txt # Optional - Python deps (can be generated via pip freeze)
```

---

## 🧪 Project Specifications

- **Language**: Python
- **Computer Vision**: OpenCV
- **Hand Tracking**: MediaPipe
- **Dependencies**:
  - `opencv-python`
  - `mediapipe`
  - `numpy`

---

## 🔮 Output
![image](https://github.com/user-attachments/assets/103ccd64-c709-47bd-80d4-605922586f04)


## 🔮 Future Plans

- 🧠 Add gesture recognition for shape drawing (e.g., circles, rectangles)
- 💾 Add save-to-image functionality (press key to save canvas)
- 🖼️ Add background image overlay option
- 📷 Toggle between webcam feed and canvas view
- 🗂️ Add UI toolbar for tool selection (instead of just gestures)
- 🎨 Color palette gesture support

---

## 🧑‍💻 Author

**Made with ❤ Nagaraj Naik**  


---

