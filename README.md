# 🚕 Uber Fare Prediction
This project is a machine learning application that predicts Uber fares in New York City based on trip details. It uses a Gradient Boosting Regressor model trained on a dataset of Uber rides. The project includes an interactive web interface built with Streamlit to provide real-time fare estimates.


## Features Used
- Distance Travelled
- Month
- Number of Passengers
- month

## Target Variable
- Fare price


## ✨ Process

-- Data Cleaning: Handles missing values, outliers, and erroneous data points.

-- Feature Engineering: Creates new, meaningful features like trip distance (using the Haversine formula) and extracts time-based features (hour, day, month, year).

-- Accurate Predictions: Utilizes a Gradient Boosting model to achieve high accuracy in fare prediction.

-- Interactive Web App: A user-friendly interface built with Streamlit to get fare estimates for custom trips.

-- Data Visualization: Includes a map to visualize the pickup and dropoff locations for the predicted trip.

## 🛠️ Tech Stack

-- Model Used : Gradient Boosting Regressor

-- Language: Python

-- Libraries:

- Scikit-learn: For machine learning model training and evaluation.

- Pandas: For data manipulation and analysis.

- NumPy: For numerical operations.

- Streamlit: For building the interactive web application.

## 📊 Dataset

The model is trained on the uber.csv dataset, which contains information about Uber rides in NYC. The key features used from the dataset are:

pickup_datetime: The timestamp when the ride started.

pickup_longitude & pickup_latitude: The coordinates of the pickup location.

dropoff_longitude & dropoff_latitude: The coordinates of the dropoff location.

passenger_count: The number of passengers in the ride.

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

Prerequisites
Python 3.8 or higher



### Installation & Usage

Clone the repository:

```
git clone [https://github.com/YourUsername/YourProjectName.git](https://github.com/YourUsername/YourProjectName.git)
cd YourProjectName
```
Create a virtual environment (recommended):
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Install the required dependencies:
A requirements.txt file should be created with the following content:
```
streamlit
pandas
numpy
scikit-learn
```

Then, run:

```
pip install -r requirements.txt
```

```
Run the Streamlit application:
Make sure your uber.csv file is in the same directory.

streamlit run app.py
```

Open your web browser and navigate to the local URL provided by Streamlit (usually http://localhost:8501).

## ⚙️ Methodology

- 1. Data Processing
     
The raw data was cleaned by removing rows with null values and filtering out trips with invalid data, such as zero fares, zero passengers, or coordinates outside of a realistic geographical range.

- 2. Feature Engineering
     
The most critical engineered feature is distance_km, calculated using the Haversine formula from the latitude and longitude coordinates. Additionally, temporal features such as hour, day_of_week, month, and year were extracted from the pickup_datetime to capture time-dependent pricing patterns.

- 3. Modeling
     
A Gradient Boosting Regressor was chosen for its high performance and accuracy. The model was trained on the engineered features to predict the fare_amount.

## 📈 Results

<img width="2701" height="2790" alt="image" src="https://github.com/user-attachments/assets/e4cb92b4-fcc8-4bc5-8317-ba8eeebbbb33" />


### Correlation Heatmap
<img width="1110" height="774" alt="image" src="https://github.com/user-attachments/assets/60e85caf-4f33-400a-8b28-7e4d713f6458" />

### Fair price with respect to Month
<img width="1061" height="658" alt="image" src="https://github.com/user-attachments/assets/c449b5d3-f3e6-4502-9d74-5a13a5289fa8" />


The model's performance on the test set is as follows:

Root Mean Squared Error (RMSE): ~21.54

R-squared (R²): ~77.63%

The model identified distance_km as the most significant factor in predicting the fare, followed by the year and geospatial features.


## Live App Link : https://uberfareprediction07.streamlit.app/

## Folder Structure
```
├── app.py              # Streamlit app
├── uber_fare.rrr           # Trained XGBoost model
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
|___1_Project.ipynb
```
## 🖼️ Application Screenshot

<img width="1341" height="746" alt="image" src="https://github.com/user-attachments/assets/304a19a7-ff6c-4857-9333-fd5fde23a5e2" />

This project was created for demonstration and learning purposes.


Author : Thiyanesh D
