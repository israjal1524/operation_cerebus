"""
Operation Cerberus - Settings

This file contains all configurable parameters for the system.
Modify values as needed before deployment.
"""

# 🔐 Voice authentication passphrase
PASS_PHRASE = "Delta Charlie Seven"

# Path to store face encodings
ENCODING_FILE = "data/face_auth.pkl"

#  Camera settings
CAMERA_INDEX = 0            # Default webcam index
FRAME_WIDTH = 640           # Camera frame width
FRAME_HEIGHT = 480          # Camera frame height

# Microphone settings
MIC_INDEX = None            # None = default system microphone
SAMPLE_RATE = 16000         # Audio sample rate in Hz
RECORD_SECONDS = 4          # Duration for voice recording

#  Liveness detection settings
BLINK_THRESHOLD = 0.25      # Eye aspect ratio threshold for blink detection
BLINK_CONSEC_FRAMES = 3     # Consecutive frames for a blink

# Debug & logging
DEBUG_MODE = True           # Show debug messages
SAVE_DEBUG_IMAGES = False   # Store frames for debugging

# System behavior
ALLOW_RETRY = True          # Allow retry after failure
MAX_ATTEMPTS = 3            # Max attempts before lockout
LOCKOUT_TIME = 60           # Lockout duration in seconds
