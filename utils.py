import numpy as np
from PIL import Image
from tensorflow.keras.applications.resnet50 import preprocess_input

from config import (
    IMG_SIZE,
    TOP_PREDICTIONS,
    VERY_HIGH_CONFIDENCE,
    HIGH_CONFIDENCE,
    MEDIUM_CONFIDENCE,
)

# ==========================================================
# Image Utilities
# ==========================================================

def load_image(uploaded_file):
    """
    Load an uploaded image and convert it to RGB.
    """
    return Image.open(uploaded_file).convert("RGB")


def resize_image(image, img_size=IMG_SIZE):
    """
    Resize image to the model input size.
    """
    return image.resize(img_size)


def preprocess_image(image, img_size=IMG_SIZE):
    """
    Convert a PIL image into a model-ready tensor.
    """
    image = resize_image(image, img_size)

    img = np.array(image, dtype=np.float32)
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)

    return img


# ==========================================================
# Prediction Utilities
# ==========================================================

def get_top_predictions(probabilities, class_names, top_k=TOP_PREDICTIONS):
    """
    Return the top-k predictions sorted by confidence.
    """

    probabilities = np.asarray(probabilities)

    indices = np.argsort(probabilities)[::-1][:top_k]

    return [
        {
            "class": class_names[idx],
            "probability": float(probabilities[idx]),
        }
        for idx in indices
    ]


# ==========================================================
# Formatting Utilities
# ==========================================================

def format_percentage(probability):
    """
    Convert probability (0-1) into a percentage.
    """
    return f"{probability * 100:.2f}%"


def confidence_label(probability):
    """
    Convert probability into a confidence label.
    """

    if probability >= VERY_HIGH_CONFIDENCE:
        return "Very High"

    if probability >= HIGH_CONFIDENCE:
        return "High"

    if probability >= MEDIUM_CONFIDENCE:
        return "Medium"

    return "Low"


def risk_label(probability):
    """
    Convert probability into a disease risk level.
    """

    if probability >= 0.90:
        return "High"

    if probability >= 0.60:
        return "Moderate"

    return "Low"


def prettify_class_name(class_name):
    """
    Convert dataset class names into a readable format.

    Example:
    Tomato___Late_blight
    ->
    Tomato - Late Blight
    """

    class_name = class_name.replace("___", " - ")
    class_name = class_name.replace("_", " ")

    return class_name.title()