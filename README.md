# 🌾 Crop Recommendation System

A machine learning–based web application that recommends the best crop to grow based on soil and environmental conditions like nitrogen, phosphorous, potassium, temperature, humidity, pH, and rainfall.

---

## 📌 Features

- Accepts user input for essential parameters
- Predicts the most suitable crop using a trained ML model
- Simple and interactive web interface using Streamlit
- Trained on real-world crop dataset

---

## 🧪 Tech Stack

- **Python**
- **Pandas, NumPy** – Data handling
- **Scikit-learn** – Model training and preprocessing
- **Streamlit** – Web interface
- **Jupyter Notebook** – Model development and experimentation

---

## 📁 Project Structure

```
Crop_Recommendation/
├── app.py                 # Streamlit application
├── model.pkl              # Trained ML model
├── scaler.pkl             # Feature scaler
├── encoder.pkl            # Label encoder
├── requirements.txt       # Environment dependencies
├── README.md              # Project overview
└── crop_recommendation.csv
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/crop-recommendation-system.git
cd crop-recommendation-system
```

### 2. (Optional) Create a virtual environment

```bash
conda create -n crop-env python=3.10
conda activate crop-env
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the App

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501` to use the crop recommender.

---

## 📌 Example Input

| Feature     | Value     |
|-------------|-----------|
| N           | 90        |
| P           | 42        |
| K           | 43        |
| Temperature | 20.87°C   |
| Humidity    | 82.00%    |
| pH          | 6.5       |
| Rainfall    | 202.93 mm |

**✅ Recommended Crop**: `rice`

---

## 🙌 Credits

- Dataset: [Kaggle – Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)
- ML Libraries: [Scikit-learn](https://scikit-learn.org/)
- Web UI: [Streamlit](https://streamlit.io/)
