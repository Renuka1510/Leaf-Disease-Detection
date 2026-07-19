"""
User Interface Components
-------------------------
Reusable Streamlit UI components for PlantVision AI.
"""

import streamlit as st


# ==========================================================
# Header
# ==========================================================

def show_header():

    st.title("🌿 Leaf Disease Detector")

    st.markdown(
        """
### Leaf Disease Detection

Upload a clear image of a plant leaf to identify diseases using a
deep learning model based on **ResNet50**.

The system provides:

- 🌱 Crop Identification
- 🦠 Disease Detection
- 📊 Confidence Score
- 🚦 Disease Risk Assessment
- 💡 Treatment Recommendation
- 📋 Top Predicted Diseases
"""
    )

    st.divider()


# ==========================================================
# Primary Result
# ==========================================================

def show_primary_result(result):

    st.subheader("🩺 Diagnosis")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Crop**")
        st.markdown(
            f"<h2 style='font-size:36px; margin-top:-10px;'>{result['crop']}</h2>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown("**Disease**")
        st.markdown(
            f"<h2 style='font-size:36px; margin-top:-10px;'>{result['primary_disease']}</h2>",
            unsafe_allow_html=True
        )


# ==========================================================
# Confidence
# ==========================================================

def show_confidence(result):

    st.subheader("📊 Prediction Confidence")

    confidence = result["confidence"]

    st.progress(confidence / 100)

    st.metric(
        "Model Confidence",
        f"{confidence:.2f}%"
    )

    st.caption(result["confidence_label"])


# ==========================================================
# Risk
# ==========================================================

def show_risk(result):

    st.subheader("🚦 Risk Assessment")

    risk = result["risk_level"]

    if risk == "No Risk":

        st.success("🟢 Healthy Plant")

    elif risk == "Low Risk":

        st.info("🟡 Low Risk")

    elif risk == "Medium Risk":

        st.warning("🟠 Medium Risk")

    else:

        st.error("🔴 High Risk")


# ==========================================================
# Description
# ==========================================================

def show_description(result):

    st.subheader("📖 Disease Description")

    st.write(result["description"])


# ==========================================================
# Recommendation
# ==========================================================

def show_recommendation(result):

    st.subheader("💡 Recommended Action")

    st.success(result["recommendation"])


# ==========================================================
# Top Predictions
# ==========================================================

def show_secondary(result):

    st.subheader("📋 Other Likely Predictions")

    predictions = result["secondary_diseases"]

    if not predictions:

        st.success(
            "The model is highly confident in a single prediction."
        )

        return

    rows = []

    for disease in predictions:

        rows.append({
            "Disease": disease["display_name"],
            "Confidence (%)": f'{disease["probability"]:.2f}'
        })

    st.dataframe(
        rows,
        use_container_width=True,
        hide_index=True
    )


# ==========================================================
# Summary
# ==========================================================

def show_summary(result):

    st.subheader("📄 Prediction Summary")

    st.markdown(f"""
| Field | Result |
|------|------|
| Crop | **{result['crop']}** |
| Disease | **{result['primary_disease']}** |
| Confidence | **{result['confidence']:.2f}%** |
| Risk | **{result['risk_level']}** |
| Severity | **{result['severity']}** |
""")


# ==========================================================
# Footer
# ==========================================================

def show_footer():

    st.divider()

    st.caption(
        "Leaf Disease Detector • Powered by ResNet50 Transfer Learning"
    )