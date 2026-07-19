import streamlit as st

from config import (
    APP_TITLE,
    APP_ICON,
    APP_LAYOUT,
    SIDEBAR_STATE,
    STYLE_PATH,
    LOGO_PATH,
    SUPPORTED_IMAGE_TYPES,
    REPORT_FILENAME
)

from utils import (
    load_image,
    confidence_label
)

from predictor import (
    load_predictor,
    predict
)

from disease_info import (
    get_disease_info
)

from multirisk import (
    assess_risk
)

from ui import *


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout=APP_LAYOUT,
    initial_sidebar_state=SIDEBAR_STATE
)


# ==========================================================
# Load CSS
# ==========================================================

try:
    with open(STYLE_PATH, "r") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )
except FileNotFoundError:
    pass


# ==========================================================
# Load Model (Cached)
# ==========================================================

@st.cache_resource
def initialize_model():
    return load_predictor()


model, class_names = initialize_model()


# ==========================================================
# Header
# ==========================================================

show_header()


# ==========================================================
# Upload Image
# ==========================================================

uploaded_file = st.file_uploader(
    "Upload a plant leaf image",
    type=SUPPORTED_IMAGE_TYPES
)

if uploaded_file is None:
    st.info("Upload a JPG, JPEG or PNG image to begin analysis.")
    st.stop()


# ==========================================================
# Load Image
# ==========================================================

image = load_image(uploaded_file)

st.image(
    image,
    caption="Uploaded Leaf Image",
    width=300
)

# ==========================================================
# Prediction
# ==========================================================

with st.spinner("Analyzing leaf image..."):

    prediction = predict(image)

    disease_info = get_disease_info(
        prediction["class_name"]
    )

    risk = assess_risk(
        prediction["class_name"],
        prediction["confidence"]
    )


# ==========================================================
# Secondary Predictions
# ==========================================================

secondary_predictions = []

for item in prediction["top_predictions"][1:]:

    info = get_disease_info(item["class"])

    secondary_predictions.append({

        "crop": info["crop"],

        "display_name": info["display_name"],

        "probability": round(
            item["probability"] * 100,
            2
        )
    })


# ==========================================================
# Final Result Dictionary
# ==========================================================

result = {

    "crop": disease_info["crop"],

    "primary_disease": disease_info["display_name"],

    "confidence": round(
        prediction["confidence"] * 100,
        2
    ),

    "confidence_label": confidence_label(
        prediction["confidence"]
    ),

    "risk_level": risk["risk_label"],

    "severity": disease_info["severity"],

    "description": disease_info["description"],

    "recommendation": disease_info["recommendation"],

    "secondary_diseases": secondary_predictions
}
# ==========================================================
# Display Results
# ==========================================================

st.divider()

show_primary_result(result)

st.divider()

col1, col2 = st.columns(2)

with col1:
    show_confidence(result)

with col2:
    show_risk(result)

st.divider()

show_description(result)

st.divider()

show_secondary(result)

st.divider()

show_recommendation(result)

st.divider()

show_summary(result)


# ==========================================================
# Generate Report
# ==========================================================

report = f"""
==================================================
            REPORT
==================================================

Crop:
{result["crop"]}

Disease:
{result["primary_disease"]}

Confidence:
{result["confidence"]:.2f}%

Confidence Level:
{result["confidence_label"]}

Risk Level:
{result["risk_level"]}

Severity:
{result["severity"]}

Description:
{result["description"]}

Recommendation:
{result["recommendation"]}

--------------------------------------------------
Other Possible Predictions
--------------------------------------------------
"""

if result["secondary_diseases"]:

    for disease in result["secondary_diseases"]:

        report += (
            f"\n• {disease['display_name']} "
            f"({disease['probability']:.2f}%)"
        )

else:

    report += "\nNone"

report += """

==================================================
Generated by Leaf Disease Detector
ResNet50 Transfer Learning
PlantVillage Dataset (38 Classes)
==================================================
"""


# ==========================================================
# Download Report
# ==========================================================

st.download_button(

    label="📥 Download Prediction Report",

    data=report,

    file_name=REPORT_FILENAME,

    mime="text/plain"

)


# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.title("🌿 Leaf Disease Detector")

    st.markdown("---")

    st.subheader("Model")

    st.write("**Architecture:** ResNet50")

    st.write("**Transfer Learning:** Yes")

    st.write("**Classes:** 38")

    st.markdown("---")

    st.subheader("Dataset")

    st.write("PlantVillage Dataset")

    st.markdown("---")

    st.subheader("Supported Formats")

    st.write("• JPG")

    st.write("• JPEG")

    st.write("• PNG")

    st.markdown("---")

    st.subheader("Features")

    st.write("✅ Disease Detection")

    st.write("✅ Multi-Risk Assessment")

    st.write("✅ Confidence Analysis")

    st.write("✅ Treatment Recommendation")

    st.write("✅ Downloadable Report")

    st.markdown("---")

    st.caption("Developed by Renuka A")


# ==========================================================
# Footer
# ==========================================================

show_footer()