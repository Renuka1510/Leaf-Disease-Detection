"""
Configuration File
------------------
Centralized configuration used throughout the project.
Modify values here instead of hardcoding them elsewhere.
"""

import os

# ==========================================================
# Base Directory
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ==========================================================
# Folder Paths
# ==========================================================

ASSETS_DIR = os.path.join(BASE_DIR, "Assets")
MODELS_DIR = os.path.join(BASE_DIR, "Models")

# ==========================================================
# Files
# ==========================================================

MODEL_PATH = os.path.join(
    MODELS_DIR,
    "ResNet50_weights_only.weights.h5"
)

CLASS_NAMES_PATH = os.path.join(
    MODELS_DIR,
    "class_names.json"
)

LOGO_PATH = os.path.join(
    ASSETS_DIR,
    "logo.png"
)

STYLE_PATH = os.path.join(
    ASSETS_DIR,
    "style.css"
)

# ==========================================================
# Image Settings
# ==========================================================

IMG_SIZE = (224, 224)

SUPPORTED_IMAGE_TYPES = [
    "jpg",
    "jpeg",
    "png"
]

# ==========================================================
# Prediction Settings
# ==========================================================

TOP_PREDICTIONS = 5

SECONDARY_THRESHOLD = 0.02

# ==========================================================
# Confidence Levels
# ==========================================================

VERY_HIGH_CONFIDENCE = 0.95
HIGH_CONFIDENCE = 0.80
MEDIUM_CONFIDENCE = 0.60

# ==========================================================
# Application Details
# ==========================================================

APP_TITLE = "Leaf Disease Detector"

APP_ICON = "🌿"

APP_LAYOUT = "wide"

SIDEBAR_STATE = "collapsed"

# ==========================================================
# Report
# ==========================================================

REPORT_FILENAME = "Leaf_Disease_Report.txt"