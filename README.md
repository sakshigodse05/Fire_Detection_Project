
🔥 Fire Detection System (Image + Video + Live Stream)

This project implements a real-time fire/combustion detection system using a combination of Deep Learning, CNN models, YOLOv3, and OpenCV.
It can detect fire in:

🔥 Live camera feed (webcam)

🔥 Uploaded videos

🔥 Individual image frames

The system also includes a GUI interface for easy interaction, login/register modules, and alert mechanisms.

🚀 Project Features
🔥 Fire Detection Using Deep Learning

Uses custom-trained CNN model (abevent.h5, abnormalevent.h5)

Supports detection on:
Images
Videos
Live camera feed
Real-time processing using OpenCV

🎥 YOLOv3-Based Object Detection

Uses:
yolov3newf.cfg
yolov3newf.weights
newf.names
Detects fire regions with bounding boxes

🖥 GUI Interface
Built using Python
Easy modules:
✔ Login
✔ Registration
✔ Detection dashboard
✔ Video/image selection

🔊 Audio Alert

Plays alarm (voice.mp4) when fire is detected

📂 Repository Structure
fire_detection_project/
│
├── fire detection videos/        # Sample videos for testing
│
├── CNNModel.py                   # CNN model for fire classification
├── video-detection.py            # Fire detection using YOLOv3 + OpenCV
├── GUI_Main (1).py               # GUI entry point
├── GUI_Master.py                 # Main GUI interface
├── GUI_Master1.py                # Extended GUI components
├── login.py                      # Login system
├── register.py                   # Registration system
│
├── yolov3newf.cfg                # YOLO configuration
├── yolov3newf.weights            # YOLO pretrained weights (large)
├── newf.names                    # Fire classes
│
├── abevent.h5                    # CNN model weights
├── abnormalevent.h5              # CNN model weights
│
├── video.mp4 / input1.mp4        # Sample input videos
├── evaluation.db                 # Database for storing logs
├── images (jpg/png/webp)         # Sample fire images
│
└── README.md                     # Project documentation

🧠 Technologies Used
Python
OpenCV
NumPy
TensorFlow / Keras (for .h5 CNN model)
YOLOv3 (Darknet)
GUI using Tkinter
SQLite Database

🛠️ How to Run the Project
1️⃣ Install Required Packages
Create a virtual environment (optional):
pip install -r requirements.txt

Typical requirements include:
opencv-python
numpy
tensorflow
keras
pillow
tkinter

2️⃣ Run the GUI Application
python GUI_Main.py

3️⃣ Run YOLO-Based Video Detection
python video-detection.py

📊 Model Details
🔥 CNN Model
Trained on a custom fire + normal dataset

Input: image frames
Output: Fire / No Fire

Architecture:
Multiple conv layers
ReLU activation
Max-pooling
Dense output layer

🎥 YOLOv3 Model
Detects flame regions
Works on both videos and live camera
Faster and more accurate for moving flames

🧪 Results
Successfully detects fire in:
Indoor/outdoor videos
Real-time camera feed
Static images
High accuracy on trained dataset
Low false positives with CNN+YOLO combined approach

📈 Future Enhancements
Add smoke detection
Deploy as a Flask API / Streamlit app
Integrate with IoT alert systems
Improve CNN architecture
Add FPS counter and performance metrics

👩‍💻 Author
Sakshi Godse
M.Tech Artificial Intelligence
GitHub: https://github.com/sakshigodse05
