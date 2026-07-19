"""
Disease Information Database
--------------------------------
Contains metadata for all PlantVillage classes.
This file is used by multirisk.py and ui.py.
"""

DISEASE_INFO = {

    # =========================
    # Apple
    # =========================

    "Apple___Apple_scab": {
        "crop": "Apple",
        "display_name": "Apple Scab",
        "healthy": False,
        "severity": "Moderate",
        "description": "Dark olive-green to brown lesions appear on leaves and may spread rapidly under humid conditions.",
        "recommendation": "Remove infected leaves, improve air circulation and apply an appropriate fungicide."
    },

    "Apple___Black_rot": {
        "crop": "Apple",
        "display_name": "Black Rot",
        "healthy": False,
        "severity": "High",
        "description": "Black rot causes circular lesions and fruit decay due to fungal infection.",
        "recommendation": "Prune infected branches and apply recommended fungicides."
    },

    "Apple___Cedar_apple_rust": {
        "crop": "Apple",
        "display_name": "Cedar Apple Rust",
        "healthy": False,
        "severity": "Moderate",
        "description": "Orange-yellow rust spots indicate fungal infection caused by cedar apple rust.",
        "recommendation": "Remove nearby cedar hosts if possible and use preventive fungicides."
    },

    "Apple___healthy": {
        "crop": "Apple",
        "display_name": "Healthy Apple Leaf",
        "healthy": True,
        "severity": "None",
        "description": "No visible disease symptoms detected.",
        "recommendation": "Continue regular monitoring and good agricultural practices."
    },

    # =========================
    # Blueberry
    # =========================

    "Blueberry___healthy": {
        "crop": "Blueberry",
        "display_name": "Healthy Blueberry Leaf",
        "healthy": True,
        "severity": "None",
        "description": "Leaf appears healthy with no visible infection.",
        "recommendation": "Maintain proper irrigation and nutrition."
    },

    # =========================
    # Cherry
    # =========================

    "Cherry_(including_sour)___Powdery_mildew": {
        "crop": "Cherry",
        "display_name": "Powdery Mildew",
        "healthy": False,
        "severity": "Moderate",
        "description": "White powdery fungal growth covers the leaf surface.",
        "recommendation": "Apply sulfur-based fungicides and improve air circulation."
    },

    "Cherry_(including_sour)___healthy": {
        "crop": "Cherry",
        "display_name": "Healthy Cherry Leaf",
        "healthy": True,
        "severity": "None",
        "description": "Healthy leaf with no disease symptoms.",
        "recommendation": "Continue routine care."
    },

    # =========================
    # Corn
    # =========================

    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "crop": "Corn",
        "display_name": "Gray Leaf Spot",
        "healthy": False,
        "severity": "Moderate",
        "description": "Rectangular gray lesions typical of Cercospora infection.",
        "recommendation": "Use resistant varieties and recommended fungicides."
    },

    "Corn_(maize)___Common_rust_": {
        "crop": "Corn",
        "display_name": "Common Rust",
        "healthy": False,
        "severity": "Moderate",
        "description": "Rust-colored pustules are visible on the leaf surface.",
        "recommendation": "Apply fungicides if infection becomes severe."
    },

    "Corn_(maize)___Northern_Leaf_Blight": {
        "crop": "Corn",
        "display_name": "Northern Leaf Blight",
        "healthy": False,
        "severity": "High",
        "description": "Large cigar-shaped lesions indicate northern leaf blight.",
        "recommendation": "Use disease-resistant hybrids and fungicide treatment."
    },

    "Corn_(maize)___healthy": {
        "crop": "Corn",
        "display_name": "Healthy Corn Leaf",
        "healthy": True,
        "severity": "None",
        "description": "Leaf appears healthy.",
        "recommendation": "Continue regular crop management."
    },

    # =========================
    # Grape
    # =========================

    "Grape___Black_rot": {
        "crop": "Grape",
        "display_name": "Black Rot",
        "healthy": False,
        "severity": "High",
        "description": "Black lesions caused by fungal infection are visible.",
        "recommendation": "Remove infected plant parts and spray fungicide."
    },

    "Grape___Esca_(Black_Measles)": {
        "crop": "Grape",
        "display_name": "Esca (Black Measles)",
        "healthy": False,
        "severity": "High",
        "description": "Leaf discoloration and necrosis indicate Esca disease.",
        "recommendation": "Remove severely infected vines and maintain vineyard hygiene."
    },

    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "crop": "Grape",
        "display_name": "Leaf Blight",
        "healthy": False,
        "severity": "Moderate",
        "description": "Brown necrotic lesions indicate grape leaf blight.",
        "recommendation": "Use recommended fungicides and remove infected leaves."
    },

    "Grape___healthy": {
        "crop": "Grape",
        "display_name": "Healthy Grape Leaf",
        "healthy": True,
        "severity": "None",
        "description": "Leaf appears healthy.",
        "recommendation": "Continue standard vineyard management."
    },

    # =========================
    # Remaining Crops
    # =========================

    "Orange___Haunglongbing_(Citrus_greening)": {
        "crop": "Orange",
        "display_name": "Citrus Greening",
        "healthy": False,
        "severity": "High",
        "description": "Serious bacterial disease causing yellow shoots and misshapen fruit.",
        "recommendation": "Control psyllid vectors and remove infected trees."
    },

    "Peach___Bacterial_spot": {
        "crop": "Peach",
        "display_name": "Bacterial Spot",
        "healthy": False,
        "severity": "Moderate",
        "description": "Dark water-soaked lesions appear on leaves.",
        "recommendation": "Apply copper-based sprays and maintain orchard sanitation."
    },

    "Peach___healthy": {
        "crop": "Peach",
        "display_name": "Healthy Peach Leaf",
        "healthy": True,
        "severity": "None",
        "description": "Healthy leaf.",
        "recommendation": "Maintain regular care."
    },

    "Pepper,_bell___Bacterial_spot": {
        "crop": "Bell Pepper",
        "display_name": "Bacterial Spot",
        "healthy": False,
        "severity": "Moderate",
        "description": "Small dark lesions caused by bacterial infection.",
        "recommendation": "Use disease-free seeds and copper sprays."
    },

    "Pepper,_bell___healthy": {
        "crop": "Bell Pepper",
        "display_name": "Healthy Bell Pepper Leaf",
        "healthy": True,
        "severity": "None",
        "description": "Healthy leaf.",
        "recommendation": "Continue regular crop care."
    },

    "Potato___Early_blight": {
        "crop": "Potato",
        "display_name": "Early Blight",
        "healthy": False,
        "severity": "Moderate",
        "description": "Target-like concentric lesions indicate early blight.",
        "recommendation": "Remove infected foliage and apply fungicides."
    },

    "Potato___Late_blight": {
        "crop": "Potato",
        "display_name": "Late Blight",
        "healthy": False,
        "severity": "High",
        "description": "Rapidly spreading water-soaked lesions caused by Phytophthora.",
        "recommendation": "Immediate fungicide treatment is recommended."
    },

    "Potato___healthy": {
        "crop": "Potato",
        "display_name": "Healthy Potato Leaf",
        "healthy": True,
        "severity": "None",
        "description": "Healthy leaf.",
        "recommendation": "Maintain normal farming practices."
    },

    "Raspberry___healthy": {
        "crop": "Raspberry",
        "display_name": "Healthy Raspberry Leaf",
        "healthy": True,
        "severity": "None",
        "description": "Healthy leaf.",
        "recommendation": "Continue routine monitoring."
    },

    "Soybean___healthy": {
        "crop": "Soybean",
        "display_name": "Healthy Soybean Leaf",
        "healthy": True,
        "severity": "None",
        "description": "Healthy soybean leaf.",
        "recommendation": "Maintain proper irrigation and fertilization."
    },

    "Squash___Powdery_mildew": {
        "crop": "Squash",
        "display_name": "Powdery Mildew",
        "healthy": False,
        "severity": "Moderate",
        "description": "White powdery fungal patches appear on leaf surfaces.",
        "recommendation": "Apply fungicides and improve ventilation."
    },

    "Strawberry___Leaf_scorch": {
        "crop": "Strawberry",
        "display_name": "Leaf Scorch",
        "healthy": False,
        "severity": "Moderate",
        "description": "Brown margins and scorched appearance are visible.",
        "recommendation": "Remove infected leaves and avoid overhead irrigation."
    },

    "Strawberry___healthy": {
        "crop": "Strawberry",
        "display_name": "Healthy Strawberry Leaf",
        "healthy": True,
        "severity": "None",
        "description": "Healthy leaf.",
        "recommendation": "Continue routine maintenance."
    },

    # =========================
    # Tomato
    # =========================

    "Tomato___Bacterial_spot": {
        "crop": "Tomato",
        "display_name": "Bacterial Spot",
        "healthy": False,
        "severity": "Moderate",
        "description": "Small dark lesions caused by bacterial infection.",
        "recommendation": "Apply copper-based bactericides."
    },

    "Tomato___Early_blight": {
        "crop": "Tomato",
        "display_name": "Early Blight",
        "healthy": False,
        "severity": "Moderate",
        "description": "Concentric ring-shaped lesions indicate early blight.",
        "recommendation": "Use fungicides and remove infected leaves."
    },

    "Tomato___Late_blight": {
        "crop": "Tomato",
        "display_name": "Late Blight",
        "healthy": False,
        "severity": "High",
        "description": "Water-soaked lesions spread rapidly across the leaf.",
        "recommendation": "Immediate fungicide application is recommended."
    },

    "Tomato___Leaf_Mold": {
        "crop": "Tomato",
        "display_name": "Leaf Mold",
        "healthy": False,
        "severity": "Moderate",
        "description": "Yellow patches with mold growth are observed.",
        "recommendation": "Reduce humidity and apply fungicide."
    },

    "Tomato___Septoria_leaf_spot": {
        "crop": "Tomato",
        "display_name": "Septoria Leaf Spot",
        "healthy": False,
        "severity": "Moderate",
        "description": "Numerous small circular lesions typical of Septoria infection.",
        "recommendation": "Remove infected leaves and apply fungicides."
    },

    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "crop": "Tomato",
        "display_name": "Spider Mites",
        "healthy": False,
        "severity": "Moderate",
        "description": "Fine yellow speckling caused by spider mite infestation.",
        "recommendation": "Apply miticides or neem oil."
    },

    "Tomato___Target_Spot": {
        "crop": "Tomato",
        "display_name": "Target Spot",
        "healthy": False,
        "severity": "Moderate",
        "description": "Target-shaped lesions indicate fungal infection.",
        "recommendation": "Use fungicides and avoid excess moisture."
    },

    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "crop": "Tomato",
        "display_name": "Tomato Yellow Leaf Curl Virus",
        "healthy": False,
        "severity": "High",
        "description": "Leaves curl upward and become yellow due to viral infection.",
        "recommendation": "Control whiteflies and remove infected plants."
    },

    "Tomato___Tomato_mosaic_virus": {
        "crop": "Tomato",
        "display_name": "Tomato Mosaic Virus",
        "healthy": False,
        "severity": "High",
        "description": "Mosaic-like discoloration is visible on the leaf.",
        "recommendation": "Remove infected plants and disinfect tools."
    },

    "Tomato___healthy": {
        "crop": "Tomato",
        "display_name": "Healthy Tomato Leaf",
        "healthy": True,
        "severity": "None",
        "description": "Leaf appears healthy with no disease symptoms.",
        "recommendation": "Continue regular monitoring and maintenance."
    }

}
# ==========================================================
# Helper Functions
# ==========================================================

DEFAULT_INFO = {
    "crop": "Unknown Crop",
    "display_name": "Unknown Disease",
    "healthy": False,
    "severity": "Unknown",
    "description": "No disease information available.",
    "recommendation": "Consult an agricultural expert."
}


def get_disease_info(class_name):
    """
    Safely fetch disease information.
    """
    return DISEASE_INFO.get(class_name, DEFAULT_INFO)


def is_healthy(class_name):
    """
    Returns True if the predicted class is healthy.
    """
    return get_disease_info(class_name)["healthy"]


def get_crop_name(class_name):
    """
    Returns crop name.
    """
    return get_disease_info(class_name)["crop"]


def get_display_name(class_name):
    """
    Returns user-friendly disease name.
    """
    return get_disease_info(class_name)["display_name"]


def get_recommendation(class_name):
    """
    Returns treatment recommendation.
    """
    return get_disease_info(class_name)["recommendation"]


def get_description(class_name):
    """
    Returns disease description.
    """
    return get_disease_info(class_name)["description"]


def get_severity(class_name):
    """
    Returns severity level.
    """
    return get_disease_info(class_name)["severity"]