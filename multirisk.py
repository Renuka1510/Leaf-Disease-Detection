"""
Multi-Disease Risk Assessment
-----------------------------
Converts model confidence and disease severity
into an easy-to-understand risk assessment.
"""

from disease_info import get_disease_info

# ==========================================================
# Risk Badge Styles
# ==========================================================

RISK_STYLE = {
    "No Risk": {
        "color": "#2E8B57",
        "icon": "🟢"
    },
    "Low Risk": {
        "color": "#6AA84F",
        "icon": "🟡"
    },
    "Medium Risk": {
        "color": "#E69138",
        "icon": "🟠"
    },
    "High Risk": {
        "color": "#CC0000",
        "icon": "🔴"
    }
}

# ==========================================================
# Severity Mapping
# ==========================================================

SEVERITY_LEVEL = {
    "None": 0,
    "Low": 1,
    "Moderate": 2,
    "High": 3
}


def assess_risk(class_name, confidence):
    """
    Returns a structured risk assessment based on
    disease severity and model confidence.
    """

    info = get_disease_info(class_name)

    severity_name = info["severity"]

    severity = SEVERITY_LEVEL.get(severity_name, 2)

    if severity == 0:
        risk_label = "No Risk"

    elif severity == 1:
        risk_label = "Low Risk"

    elif severity == 2:
        risk_label = "Medium Risk"

    else:
        risk_label = "High Risk"

    # Escalate one level if confidence is extremely high
    if confidence >= 0.95:

        if risk_label == "Low Risk":
            risk_label = "Medium Risk"

        elif risk_label == "Medium Risk":
            risk_label = "High Risk"

    risk_score = round(confidence * severity, 3)

    return {
        "predicted_class": class_name,
        "confidence": round(float(confidence), 4),
        "severity": severity_name,
        "severity_level": severity,
        "risk_score": risk_score,
        "risk_label": risk_label,
        "style": RISK_STYLE[risk_label]
    }