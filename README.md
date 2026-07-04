# ❤️ Heart Disease Prediction using Random Forest

A machine learning-based web application that predicts the likelihood of heart disease using patient health information. This project utilizes the **Random Forest Classifier** for accurate predictions and **Streamlit** for an interactive and user-friendly web interface.

---

## 📖 Overview

Heart disease remains one of the leading causes of death worldwide. Early identification of individuals at risk can support timely medical intervention and improve healthcare outcomes.

This project applies machine learning techniques to analyze patient medical data and predict the presence of heart disease. The application is designed to provide quick predictions through an intuitive Streamlit interface.

---

## ✨ Features

* Interactive web application built with Streamlit
* Heart disease prediction using the Random Forest algorithm
* Clean and user-friendly interface
* Fast and accurate predictions
* Data preprocessing and model training
* Easy deployment and accessibility

---

## 🛠️ Technologies Used

* Python 3.x
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Joblib/Pickle

---

## 📂 Project Structure

```text
Heart-Disease-Prediction/
│
├── dataset/
│   └── heart.csv
├── model/
│   └── random_forest_model.pkl
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── images/
    └── screenshot.png
```

---

## 📊 Dataset

The dataset contains important patient health attributes, including:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting Electrocardiographic Results
* Maximum Heart Rate Achieved
* Exercise-Induced Angina
* ST Depression (Oldpeak)
* Slope of ST Segment
* Number of Major Vessels
* Thalassemia

### Target Variable

* **0** – No Heart Disease
* **1** – Heart Disease

---

## 🤖 Machine Learning Model

This project uses the **Random Forest Classifier**, an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

### Why Random Forest?

* High prediction accuracy
* Handles complex datasets effectively
* Resistant to overfitting
* Works well with both numerical and categorical features
* Provides feature importance analysis

---

## 📈 Model Evaluation

The model performance is evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* ROC-AUC Score

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Heart-Disease-Prediction.git
```

### 2. Navigate to the project folder

```bash
cd Heart-Disease-Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

---

## 🚀 Usage

1. Launch the Streamlit application.
2. Enter the patient's medical details.
3. Click the **Predict** button.
4. The application displays whether the patient is at risk of heart disease.

---

## 📷 Screenshots

Include screenshots such as:

* Patient Input Form
![alt text](heart1-2.png)
* Prediction Result
![alt text](heart2-1.png)

---

## 📌 Future Enhancements

* Hyperparameter tuning for improved accuracy
* Deployment on Streamlit Community Cloud
* REST API integration
* Additional visualization dashboards
* Support for larger cardiovascular datasets
* Model explainability using SHAP or LIME

---

## 🙏 Acknowledgement

* Kaggle for providing the Heart Disease dataset.
* The **Scikit-learn** team for their comprehensive machine learning library.
* The **Streamlit** team for making web application development simple and efficient.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork this repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.
