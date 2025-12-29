# Real-time Violence Analysis & Monitoring System

A modular video processing system for detecting fights and tracking people using YOLO models.

## Features

- **Fight Detection**: Detects fights in video footage using a custom-trained YOLO model
- **Person Tracking**: Tracks individuals and identifies those involved in fights
- **Advanced Dashboard**: Real-time visualization with:
  - Fight status indicator with pulsing effects
  - Total people count
  - Fighting people identification
  - Fight intensity bar with gradient
  - Frequency graph showing fight intensity over time
- **Ghost Box Persistence**: Reduces flickering by maintaining detection boxes for a few frames
- **Temporal Confirmation**: Requires multiple frames to confirm a fight, reducing false positives
- **Multi-Video Processing**: Processes and merges multiple video files into a single output

## Project Structure

```
fight_detection/
├── config.py                    # Configuration and constants
├── utils/                       # Utility functions
│   ├── __init__.py
│   ├── drawing.py              # Drawing utilities (text with background)
│   └── geometry.py             # Geometric utilities (overlap checks)
├── visualization/               # Visualization components
│   ├── __init__.py
│   └── dashboard.py            # Advanced dashboard rendering
├── detection/                   # Detection modules
│   ├── __init__.py
│   ├── fight_detector.py       # Fight detection logic
│   └── person_tracker.py       # Person tracking logic
├── processing/                  # Video processing pipeline
│   ├── __init__.py
│   └── video_processor.py      # Main video processing orchestrator
├── main.py                      # Entry point
└── README.md                    # This file
```

## Requirements

- Python 3.8+
- OpenCV (`cv2`)
- Ultralytics YOLO (`ultralytics`)

## Installation

1. Install required packages:
```bash
pip install opencv-python ultralytics
```

2. Ensure you have the required YOLO models:
   - Fight detection model (custom trained)
   - Person detection model (YOLO11x or similar)

## Configuration

Edit `config.py` to customize:

- **Model Paths**: Paths to your YOLO model weights
- **Video Paths**: List of input videos to process
- **Output Path**: Where to save the processed video
- **Detection Parameters**: Confidence thresholds, image size
- **Temporal Settings**: Window size and fight trigger threshold
- **Dashboard Settings**: Colors, fonts, scaling factors

## Usage

Simply run the main script:

```bash
python main.py
```

The system will:
1. Load the YOLO models
2. Process each video in the configured list
3. Detect fights and track people
4. Draw the advanced dashboard overlay
5. Save the merged output video
6. Display processing statistics

### Keyboard Controls

- **Q**: Quit processing early

## How It Works

### Fight Detection

1. Each frame is analyzed using a custom-trained YOLO model
2. Fight detections above the confidence threshold are identified
3. A "ghost box" mechanism maintains detection for a few frames to reduce flickering
4. Temporal logic requires multiple detections within a window to confirm a fight

### Person Tracking

1. YOLO model detects and tracks all people in the frame
2. Each person is assigned a unique ID
3. People whose center point falls within a fight box are marked as "fighting"
4. Person labels are drawn at the center of each detected person

### Dashboard

The dashboard displays three sections:
- **Left**: Fight status (SAFE/ACTIVE) and total people count
- **Middle**: Fighting people IDs and intensity bar
- **Right**: Real-time frequency graph of fight intensity

## Customization

### Adding New Videos

Edit `config.py` and add paths to `VIDEO_PATHS` list:

```python
VIDEO_PATHS = [
    r"path\to\video1.avi",
    r"path\to\video2.avi",
    # Add more videos here
]
```

### Adjusting Detection Sensitivity

In `config.py`:

```python
CONF_THRESHOLD = 0.15  # Lower = more sensitive, higher = more strict
FIGHT_TRIGGER = 6      # Frames needed in window to confirm fight
WINDOW = 15            # Size of temporal window
```

### Changing Dashboard Colors

In `config.py`, modify the color constants (BGR format):

```python
COLOR_FIGHT = (0, 0, 255)  # Red for fight
COLOR_SAFE = (0, 255, 0)   # Green for safe
COLOR_PERSON = (255, 0, 0) # Blue for person labels
```

## Output

The system generates:
- A merged video file with all detections and dashboard overlay
- Console output showing processing progress
- Final statistics including:
  - Total frames processed
  - Frames with confirmed fights
  - Fight percentage

## Troubleshooting

**Issue**: "Could not open video"
- Check that video paths in `config.py` are correct
- Ensure video files exist and are readable

**Issue**: Model not found
- Verify model paths in `config.py`
- Ensure YOLO model files are downloaded and accessible

**Issue**: Poor detection quality
- Adjust `CONF_THRESHOLD` in `config.py`
- Consider retraining the fight detection model with more data

## 👤 Author

**HOSEN ARAFAT**  

**Software Engineer, China**  

**GitHub:** https://github.com/arafathosense

**Researcher: Artificial Intelligence, Machine Learning, Deep Learning, Computer Vision, Image Processing**
