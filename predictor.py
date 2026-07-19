import json
import time
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.layers import (
    Input,
    Dense,
    Dropout,
    GlobalAveragePooling2D
)
from tensorflow.keras.applications import ResNet50

from huggingface_hub import hf_hub_download

from config import (
    MODEL_PATH,
    CLASS_NAMES_PATH,
    IMG_SIZE,
    TOP_PREDICTIONS
)

from utils import (
    preprocess_image,
    get_top_predictions
)

# ==========================================================
# Hugging Face Model Details
# ==========================================================

HF_REPO_ID = "renuka-1510/leaf-disease-resnet50"
HF_FILENAME = "ResNet50_weights_only.weights.h5"


# ==========================================================
# Download Model if Missing
# ==========================================================

def ensure_model_exists():
    """
    Downloads the model from Hugging Face if it doesn't exist locally.
    """

    if os.path.exists(MODEL_PATH):
        return

    print("Downloading model from Hugging Face...")

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

    hf_hub_download(
        repo_id=HF_REPO_ID,
        filename=HF_FILENAME,
        local_dir=os.path.dirname(MODEL_PATH),
        local_dir_use_symlinks=False
    )

    print("Model downloaded successfully.")


# ==========================================================
# Model Architecture
# ==========================================================

def build_model():
    """
    Build the ResNet50 model architecture and load trained weights.
    """

    ensure_model_exists()

    base_model = ResNet50(
        include_top=False,
        weights=None,
        input_shape=(*IMG_SIZE, 3)
    )

    inputs = Input(shape=(*IMG_SIZE, 3))

    x = base_model(inputs, training=False)

    x = GlobalAveragePooling2D()(x)

    x = Dropout(0.3)(x)

    outputs = Dense(
        38,
        activation="softmax",
        dtype="float32"
    )(x)

    model = Model(inputs, outputs)

    model.load_weights(MODEL_PATH)

    return model


# ==========================================================
# Load Class Names
# ==========================================================

def load_class_names():
    with open(CLASS_NAMES_PATH, "r") as file:
        return json.load(file)


# ==========================================================
# Cached Objects
# ==========================================================

_model = None
_class_names = None


def load_predictor():

    global _model
    global _class_names

    if _model is None:

        start = time.time()

        print("Building model...")

        _model = build_model()

        print("Model build:", time.time() - start)

        start = time.time()

        _class_names = load_class_names()

        print("Class names:", time.time() - start)

    return _model, _class_names


# ==========================================================
# Prediction
# ==========================================================

def predict(image, top_k=TOP_PREDICTIONS):
    """
    Predict the disease from a PIL image.
    """

    model, class_names = load_predictor()

    processed_image = preprocess_image(image)

    probabilities = model.predict(
        processed_image,
        verbose=0
    )[0]

    predicted_index = int(tf.argmax(probabilities))

    top_predictions = get_top_predictions(
        probabilities,
        class_names,
        top_k
    )

    return {
        "class_name": class_names[predicted_index],
        "confidence": float(probabilities[predicted_index]),
        "probabilities": probabilities,
        "top_predictions": top_predictions
    }