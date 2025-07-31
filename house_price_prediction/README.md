# House Price Prediction using Linear Regression

This project predicts house prices using a Linear Regression model on the California housing dataset. It involves data preprocessing, feature engineering, training the model, and visualizing results.

## 📁 Dataset
The dataset used is `housing.csv`, which contains information such as:
- Geolocation (`longitude`, `latitude`)
- Housing features (`total_rooms`, `total_bedrooms`, `households`, etc.)
- Categorical feature: `ocean_proximity`
- Target variable: `median_house_value`

## 📊 Features Engineering
- `rooms_per_household` = total_rooms / households
- `bedrooms_per_room` = total_bedrooms / total_rooms
- `population_per_household` = population / households
- Log transformation on skewed features
- One-hot encoding for `ocean_proximity`
- Scaling using `StandardScaler`

## 🧠 Model
- **Model**: Linear Regression
- **Library**: Scikit-learn
- **Evaluation Metrics**:
  - R² Score
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
  - Root Mean Squared Error (RMSE)
  - Mean Absolute Percentage Error (MAPE)
  - Accuracy = 100 - MAPE

## 📈 Visualizations
- Correlation heatmap of all numerical features
- Actual vs Predicted price scatter plot

## 🛠️ Requirements
Install all required packages using:

```
pip install -r requirements.txt
```

## 📂 Project Structure
```
├── housing.csv
├── model.py
├── requirements.txt
└── README.md
```

## ✅ How to Run
1. Make sure Python 3 is installed.
2. Install dependencies using pip.
3. Run the `model.py` script:
```bash
python model.py
```

## 🔍 Output
- Regression metrics printed in terminal
- Correlation heatmap
- Actual vs Predicted plot