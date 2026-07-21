# 🥇 Gold Price Prediction using Machine Learning

A Machine Learning project that predicts gold prices based on market-related features using multiple regression algorithms. The project includes data preprocessing, exploratory data analysis (EDA), model training, evaluation, and deployment using Streamlit.

---

## 📌 Project Overview

The objective of this project is to predict the price of gold using historical market data. Different regression models were trained and compared to identify the best-performing model. Finally, the best model was saved and deployed as an interactive Streamlit web application.

---

## 📂 Dataset

The dataset contains historical gold price information along with several financial indicators, including:

- SPX (S&P 500 Index)
- USO (United States Oil Fund)
- SLV (Silver Price)
- EUR/USD Exchange Rate
- Gold Price (Target Variable)

---

## 🚀 Project Workflow

- Data Loading
- Data Exploration
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Selection
- Train-Test Split
- Model Training
- Model Evaluation
- Model Comparison
- Model Saving
- Streamlit Deployment

---

## 📊 Exploratory Data Analysis

The following visualizations were performed:

- Pair Plot
- Correlation Heatmap
- Distribution Plot
- Box Plot
- Feature Importance Plot
- Actual vs Predicted Plot

---

## 🤖 Machine Learning Models Used

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

---

## 📈 Model Evaluation Metrics

The models were evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)

The **Random Forest Regressor** achieved the best performance and was selected as the final model.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Pickle

---

## 📁 Project Structure

```
gold-price-prediction/
│
├── Gold Price Prediction.ipynb
├── app.py
├── rf_model.pkl
├── requirements.txt
├── README.md
└── gld_price_data.csv
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/gold-price-prediction.git
```

Navigate to the project directory

```bash
cd gold-price-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📸 Application Preview

<img width="900" alt="Application Screenshot" src="images/app.png">

> Replace the above image with a screenshot of your Streamlit application after deployment.

---

## 🎯 Results

- Successfully trained multiple regression models.
- Compared model performance using standard regression metrics.
- Random Forest Regressor achieved the highest prediction accuracy.
- Deployed the best-performing model using Streamlit for real-time predictions.

---

## 🔮 Future Improvements

- Hyperparameter Tuning
- Cross Validation
- Feature Engineering
- Model Explainability (SHAP)
- Cloud Deployment
- Live Gold Price API Integration

---

## 👨‍💻 Author

**Kousik Chakraborty**

Aspiring Data Analyst | Machine Learning Enthusiast


## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
