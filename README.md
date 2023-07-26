# Indian-Flight-Fare-Prediction


##### Author: Syed Mohammad Afraim

##### Date: 26th July, 2023

##### [Kaggle](https://www.kaggle.com/code/syedmohammadafraim2/flight-fare-prediction)

# 1. Summary <a name="summary_1"></a>
This project aims to predict flight fares based on various features such as departure date and time, arrival date and time, total stops, airline, source, and destination. The prediction model is built using a RandomForestRegressor algorithm.

# 2. Ask Phase <a name="ask_phase_2"></a>
## Business Task <a name="business_task_2_1"></a>
The business task in this project is to develop a predictive model that can accurately estimate the flight fares based on the given features. This will help travelers plan their trips more effectively and make informed decisions about flight bookings.

# 3. Prepare Phase <a name="prepare_phase_3"></a>
## 3.1 Dataset Used <a name="dataset_used_3_1"></a>
The dataset used for this project is obtained from Kaggle and contains information about various flight routes, airlines, and their corresponding fares. The dataset can be accessed from the following link: [Flight Fare Prediction Dataset](https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh)

## 3.2 Accessibility and Privacy of Data <a name="accessibility_and_privacy_of_data_3_2"></a>
The dataset used is publicly accessible from Kaggle, and it does not contain any sensitive or private information about individuals.

## 3.3 Information about Our Dataset <a name="information_about_our_dataset_3_3"></a>
The dataset consists of columns such as departure date and time, arrival date and time, total stops, airline, source, destination, and flight fares.

## 3.4 Data Organization and Verification <a name="data_organization_and_verification_3_4"></a>
The dataset is organized and cleaned to remove any missing or erroneous data. Data verification is performed to ensure its integrity and accuracy.

## 3.5 Data Credibility and Integrity <a name="data_credibility_and_integrity_3_5"></a>
The dataset used in this project is from a reputable source, and steps are taken to maintain the credibility and integrity of the data throughout the project.

## 3.6 Feature Selection and Model Building <a name="feature_selection_and_model_building_3_6"></a>
In the Prepare Phase, feature selection techniques such as correlation matrix, heatmap, Extra Trees Regressor, and Recursive Feature Elimination with Cross-Validation (RFECV) were used to select the most important features for model building. The RandomForestRegressor algorithm was chosen as the final model, and hyperparameter tuning was performed using RandomizedSearchCV for improved performance.

# Conclusion <a class= 'anchor' id = conc></a>
This project demonstrates the development of a predictive model for flight fare estimation using machine learning techniques. The model can be used to make informed decisions about flight bookings and plan trips more effectively. The dataset used in the project is publicly available and sourced from Kaggle. Various feature selection and model building techniques were applied to create an accurate and reliable prediction model.

The project is also available at [flights-fare.onrender.com](flights-fare.onrender.com), where the business phase or ask phase has been successfully achieved. Users can access the deployed application to predict flight fares based on their preferred flight details. The model's performance has been improved through feature selection and hyperparameter tuning, ensuring a better user experience and more accurate predictions.

By leveraging machine learning techniques, this project provides valuable insights into predicting flight fares, empowering travelers to plan their trips efficiently and make informed decisions about their flight bookings.