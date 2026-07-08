# 💻 Laptop Price Predictor

A Machine Learning web application that predicts the price of a laptop based on its hardware specifications. The project demonstrates a complete end-to-end ML workflow including data cleaning, exploratory data analysis, feature engineering, model selection, ensemble learning, model serialization, deployment, and an interactive Streamlit interface.

---

## 📌 Features

- Predicts laptop prices instantly
- Interactive and user-friendly Streamlit interface
- Automatic screen PPI calculation
- Ensemble Voting Regressor for improved prediction accuracy
- Handles categorical and numerical features using a preprocessing pipeline
- End-to-end machine learning workflow

---

## 📂 Project Structure

```
Laptop-Price-Predictor/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── laptop_data.csv
│   ├── clean_data.csv
│   └── df.pkl
│
├── notebooks/
│   ├── EDA.ipynb
│   └── Model_Training.ipynb
│
├── models/
    └── model.pkl

```

---

## 📊 Dataset

The dataset contains specifications of various laptops including:

- Brand
- Type
- RAM
- Weight
- Touchscreen
- IPS Display
- Screen Resolution
- CPU
- HDD
- SSD
- GPU
- Operating System
- Price

---

## 🛠 Data Preprocessing

The following preprocessing steps were performed:

- Missing value handling
- Duplicate removal
- Feature engineering
- Screen PPI calculation
- CPU Brand extraction
- GPU Brand extraction
- Operating System categorization
- Memory feature transformation
- Removal of unnecessary columns
- One-Hot Encoding using ColumnTransformer

---

## 📈 Exploratory Data Analysis

EDA includes:

- Distribution plots
- Correlation analysis
- Feature importance study
- Price distribution
- Brand-wise comparison
- RAM analysis
- Storage analysis
- CPU analysis
- GPU analysis
- Operating System analysis

---

## 🤖 Machine Learning Models Evaluated

The following regression algorithms were tested:

- Linear Regression
- Ridge Regression
- Lasso Regression
- K Nearest Neighbors Regressor
- Support Vector Regressor
- Decision Tree Regressor
- Random Forest Regressor
- Extra Trees Regressor
- AdaBoost Regressor
- Gradient Boosting Regressor
- XGBoost Regressor
- Voting Regressor
- Stacking Regressor

---

## 🏆 Final Model

The best performing model was:

**Voting Regressor**

Base Models:

- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor
- Extra Trees Regressor

The preprocessing pipeline and model were combined using Scikit-Learn Pipeline and saved using Pickle.

---

## ⚙️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-Learn
- XGBoost
- Streamlit
- Pickle

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/Ankitathakur30/Laptop-Price-Predictor.git
```

Move into the project

```bash
cd Laptop-Price-Predictor
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

## 🎯 How to Use

1. Select laptop brand.
2. Choose laptop type.
3. Enter RAM.
4. Enter laptop weight.
5. Select touchscreen option.
6. Select IPS option.
7. Enter screen size.
8. Select screen resolution.
9. Select CPU.
10. Select HDD capacity.
11. Select SSD capacity.
12. Select GPU.
13. Select Operating System.
14. Click **Predict Price**.

The application instantly estimates the laptop price.

---


## 📊 Future Improvements

- Deep Learning models
- Hyperparameter Optimization using Optuna
- Explainable AI using SHAP
- Model Monitoring
- Docker Containerization
- CI/CD Pipeline
- Cloud Deployment on AWS

---

## 👩‍💻 Author

**Ankita Thakur**

B.Tech Computer Science Engineering

Machine Learning | Python | Data Science | AI

GitHub: https://github.com/Ankitathakur30

LinkedIn:https://www.linkedin.com/in/ankita-thakur-061b00380?utm_source=share_via&utm_content=profile&utm_medium=member_androidnkedin.com/in/YourLinkedIn

---

## ⭐ If you found this project useful, consider giving it a Star!