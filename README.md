# Horse Racing Prediction Model

## Project Overview

This project aims to develop a predictive model for estimating the position of a horse in a race using various features such as race details, horse attributes, and historical performance. The goal is to leverage machine learning techniques to create an accurate and reliable model.

## **Data Preprocessing and Feature Engineering**

1. **Frequency Encoding**: Applied to categorical columns.
2. **Date Features**: Extracted month, day, day of the week, and year from the `date` column.
3. **New Features**:
   - **place_rate**: Calculated as `res_place / runners`.
   - **average_margin**: Calculated as `margin / runners`.
   - **weight_diff**: Calculated as `weightSt - weightLb`.
4. **Handling Missing Values**: Used forward fill followed by backward fill.
5. **Scaling**: StandardScaler applied to numerical columns.

## **Model Building and Evaluation**

1. **Train-Test Split**: Divided the dataset into training and testing sets (80-20 split).
2. **Model Training**: Used Random Forest Regressor and Lasso Regression.
3. **Hyperparameter Tuning**: Performed Grid Search for Random Forest to find the best parameters.
4. **Feature Importance**: Assessed using Random Forest and Mutual Information.

## **Features Selected by RFE**

The Recursive Feature Elimination (RFE) method identified the following top 10 features as the most significant:
1. **winningTime**
2. **prize**
3. **positionL**
4. **dist**
5. **RPR**
6. **TR**
7. **OR**
8. **runners**
9. **res_place**
10. **average_margin**

## **Model Performance**

### **Random Forest Regressor**
- **R² Score**: 0.8243
- **Mean Squared Error (MSE)**: 0.1750
- **Cross-validation Mean Score**: 0.7963

#### **Best Model Parameters (After Hyperparameter Tuning)**
- **Best R² Score**: 0.8247
- **Best MSE**: 0.1746
- **Best Hyperparameters**: 
  - **max_depth**: 20
  - **min_samples_split**: 2
  - **n_estimators**: 200

### **Lasso Regression**
- **R² Score**: 0.5980
- **Mean Squared Error (MSE)**: 0.4004


