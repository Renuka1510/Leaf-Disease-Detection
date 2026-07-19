# 🌿 Leaf Disease Detection

An AI-powered web application for detecting plant leaf diseases using **ResNet50 Transfer Learning** and providing **Multi-Risk Assessment**, disease information, and treatment recommendations.

---

## 📖 Overview

This project uses a deep learning model trained on the **PlantVillage Dataset** to classify plant leaf diseases. The application allows users to upload a leaf image and receive:

- 🌱 Crop Identification
- 🦠 Disease Detection
- 📊 Prediction Confidence
- 🚦 Multi-Risk Assessment
- 📖 Disease Description
- 💡 Treatment Recommendation
- 📋 Other Likely Predictions

---

## 🚀 Features

- Deep Learning-based Disease Detection
- ResNet50 Transfer Learning
- Confidence Analysis
- Multi-Risk Assessment
- Disease Information Database
- Interactive Streamlit Web Interface
- Downloadable Prediction Report

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Deep Learning | TensorFlow / Keras |
| Model | ResNet50 |
| Frontend | Streamlit |
| Dataset | PlantVillage |

---

## 📂 Project Structure

```text
Leaf-Disease-Detection/
│
├── Assets/
│   └── style.css
│
├── Models/
│   ├── class_names.json
│   └── ResNet50_weights_only.weights.h5
│
├── app.py
├── predictor.py
├── multirisk.py
├── disease_info.py
├── ui.py
├── utils.py
├── config.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Renuka1510/Leaf-Disease-Detection.git
```

Move into the project directory

```bash
cd Leaf-Disease-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📊 Model Performance

- Model: ResNet50
- Validation Accuracy: **97.5%**
- Transfer Learning with Fine-Tuning
- Trained on PlantVillage Dataset

---

## 📌 Dataset

PlantVillage Dataset

Contains images from multiple crops including:

- Apple
- Cherry
- Corn
- Grape
- Peach
- Pepper
- Potato
- Strawberry
- Tomato

and more.

---

## 🔮 Future Improvements

- Support for real-world field images
- Mobile application
- Disease severity estimation
- Automatic treatment scheduling
- Cloud deployment

---

## 👩‍💻 Author

**Renuka A**

Final Year B.Tech Student

Computer Science & Engineering (Cyber Security)

Manipal Institute of Technology

---

## ⭐ If you found this project useful, consider giving it a star.