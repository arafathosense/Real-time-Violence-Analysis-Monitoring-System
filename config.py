"""
Configuration module for fight detection system.
Contains all settings, paths, and constants.
"""

# ========================
# MODEL PATHS
# ========================
FIGHT_MODEL_PATH = r"c:\Users\PC\Documents\fight\train4\weights\last.pt"
PERSON_MODEL_PATH = r"c:\Users\PC\yolo11x.pt"

# ========================
# VIDEO PATHS
# ========================
VIDEO_PATHS = [
    r"c:\Users\PC\Desktop\New folder (2)\y_vX9FtjLaQ_0.avi",
    r"c:\Users\PC\Desktop\New folder (2)\y_vX9FtjLaQ_3.avi",
    
    r"c:\Users\PC\Desktop\New folder (2)\y_vX9FtjLaQ_1.avi",
    r"c:\Users\PC\Desktop\New folder (2)\b6XfVAZC9Zs_1.avi",
    r"c:\Users\PC\Desktop\New folder (2)\b6XfVAZC9Zs_2.avi",
    r"c:\Users\PC\Desktop\New folder (2)\b6XfVAZC9Zs_3.avi",
    r"c:\Users\PC\Desktop\New folder (2)\b6XfVAZC9Zs_4.avi",
    r"c:\Users\PC\Desktop\New folder (2)\b6XfVAZC9Zs_6.avi",
    
    r"c:\Users\PC\Desktop\New folder (2)\\_RziL1Ds6xU_1.avi",
    r"c:\Users\PC\Desktop\New folder (2)\\_RziL1Ds6xU_0.avi",

    r"c:\Users\PC\Desktop\New folder (2)\Wby1vUy8aYI_0.avi",

    r"c:\Users\PC\Desktop\New folder (2)\DTq6Gu30-uA_3.avi",
    
    r"c:\Users\PC\Desktop\New folder (2)\DTq6Gu30-uA_5.avi",
    
    r"C:\Users\PC\Downloads\archive\RWF-2000\train\Fight\sadsa_959.avi",
    r"C:\Users\PC\Downloads\archive\RWF-2000\train\Fight\sadsa_957.avi",
    r"C:\Users\PC\Downloads\archive\RWF-2000\train\Fight\sadsa_958.avi",

    r"c:\Users\PC\Desktop\New folder (2)\1122 (2).avi",
    r"c:\Users\PC\Desktop\New folder (2)\1122 (3).avi",
    r"c:\Users\PC\Desktop\New folder (2)\1122 (1).avi",
]

OUTPUT_PATH = r"c:\Users\PC\Documents\fight\output_fight_detection.mp4"

# ========================
# DETECTION PARAMETERS
# ========================
CONF_THRESHOLD = 0.15
IMG_SIZE = 960
PERSON_CONF_THRESHOLD = 0.3

# ========================
# TEMPORAL WINDOW SETTINGS
# ========================
WINDOW = 15          # frames
FIGHT_TRIGGER = 6    # minimum frames in window to confirm fight

# ========================
# PERSISTENCE SETTINGS
# ========================
MAX_PATIENCE = 10    # frames to keep ghost box after fight disappears

# ========================
# GRAPH SETTINGS
# ========================
GRAPH_HISTORY_SIZE = 100  # number of intensity values to store

# ========================
# VIDEO OUTPUT SETTINGS
# ========================
FOURCC = 'XVID'  # Video codec
DEFAULT_FPS = 25  # Default FPS if video metadata is unavailable

# ========================
# DASHBOARD COLORS (BGR)
# ========================
COLOR_BG = (0, 0, 0)           # Black background
COLOR_BORDER = (255, 255, 255) # White border
COLOR_FIGHT = (0, 0, 255)      # Red for fight
COLOR_SAFE = (0, 255, 0)       # Green for safe
COLOR_PERSON = (255, 0, 0)     # Blue for person labels
COLOR_TEXT_BG = (255, 255, 255) # White background for text

# ========================
# DASHBOARD SETTINGS
# ========================
DASHBOARD_ALPHA = 0.8  # Transparency for dashboard panels
DASHBOARD_SCALE_MAX = 1.2  # Maximum scale factor for large videos
