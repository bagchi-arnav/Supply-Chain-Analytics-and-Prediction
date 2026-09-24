# Supply Chain Delivery Analytics

## Project Overview
This project is an end-to-end data analytics and machine learning project focused on analyzing supply chain delivery performance and understanding the factors associated with late deliveries.

The project covers data cleaning, exploratory data analysis, business and root-cause analysis, feature engineering, machine learning, model evaluation, and deployment of a late-delivery prediction application using Streamlit.

**Dataset:** [SupplyChainDataset.csv](https://drive.google.com/file/d/1tCG3E_KeuFwxn5Roobaz4FVBR5dQWEMr/view?usp=sharing)

## Business Problem
Late deliveries can affect customer satisfaction, operational efficiency, and overall supply chain performance. The objective of this project is to analyze historical order and shipment data to identify the major factors associated with delivery delays and develop a model that can predict whether a new order is likely to be delivered late.

## Project Objectives

- Analyze historical supply chain and delivery data to understand delivery performance.
- Identify the major operational factors associated with late deliveries.
- Perform exploratory and root-cause analysis using relevant business metrics.
- Engineer features suitable for machine learning.
- Develop and evaluate classification models for late-delivery prediction.
- Select a suitable predictive model for deployment.
- Build a simple Streamlit application that allows users to predict the delivery status of a new order.

## Data Analysis

The analysis includes data cleaning, exploratory data analysis, feature engineering, and business-focused investigation of delivery delays.

Key areas analyzed include:

- Delivery status and delay patterns
- Shipping mode performance
- Order timing and temporal patterns
- Regional and market-level delivery performance
- Operational factors associated with late deliveries
- Relationship between delivery performance and business metrics

The analysis was used to identify potential drivers of delivery delays before developing the predictive models.

## Key Findings

The analysis indicated that shipping mode was one of the most important operational factors associated with delivery delays.
Further analysis showed that order timing features also contributed to the prediction of late deliveries, while regional and market-level differences were comparatively less prominent.These findings were used to guide the feature engineering and machine learning stages of the project.

## Machine Learning

The project uses supervised classification to predict whether an order will result in a late delivery.

The machine learning workflow included:

- Feature preparation and frequency encoding of categorical variables
- Train-test split
- Handling class imbalance using SMOTE
- Training multiple classification models
- Evaluating model performance using classification metrics
- Comparing models to identify a suitable model for deployment

The models evaluated included:

- Logistic Regression
- Decision Tree
- Random Forest

## Model Performance

After applying SMOTE to address class imbalance, three classification models were evaluated on the test set.

| Model | Test Accuracy |
|---|---:|
| Logistic Regression | 69.70% |
| Decision Tree | 78.24% |
| Random Forest | 76.33% |

### Model Selection

The Decision Tree achieved the highest test accuracy at 78.24%.
Random Forest was selected for deployment because it is an ensemble model that combines multiple decision trees, providing a more robust modeling approach than relying on a single tree.The deployed prediction system therefore uses the Random Forest model.

## Deployment

The trained prediction pipeline was integrated into a Streamlit web application.

The application allows a user to enter order and shipment characteristics and receive:

- Predicted delivery status
- Probability of late delivery

The deployment architecture separates the trained model and preprocessing components from the user interface, allowing the same prediction pipeline to be reused by the application.

## Technologies Used

- **Python** — Data analysis, preprocessing, feature engineering, and machine learning
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical operations
- **Matplotlib & Seaborn** — Data visualization
- **Scikit-learn** — Machine learning models and evaluation
- **imbalanced-learn (SMOTE)** — Handling class imbalance
- **Joblib** — Saving and loading trained model components
- **Jupyter Notebook** — Data analysis and experimentation
- **Streamlit** — Web application and model deployment

## Project Structure

```text
Supply-Chain-Delivery-Analytics/
│
├── main.ipynb
│
├── app.py
├── predictor.py
├── test_predictor.py
│
├── frequency_maps.pkl
├── feature_columns.pkl
│
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/bagchi-arnav/Supply-Chain-Analytics-and-Prediction.git
cd Supply-Chain-Analytics-and-Prediction
```

### 2. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app.py
```
The application will open in your browser and allow you to enter order details and generate a late-delivery prediction. 

## Results & Conclusion

The project combines data analytics and machine learning to investigate supply chain delivery performance and predict the likelihood of late deliveries.

The analysis identified shipping mode and order timing as important factors associated with delivery delays. The machine learning stage demonstrated that the delivery status of an order can be predicted using historical order and shipment characteristics.

The final system extends the analytical work into a practical prediction application through Streamlit.
