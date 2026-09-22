import joblib
import pandas as pd

pd.set_option("display.max_columns", None)

model = joblib.load("late_delivery_model.pkl")
frequency_maps = joblib.load("frequency_maps.pkl")
feature_columns = joblib.load("feature_columns.pkl")

def predict_order(user_input):
    """
    Predict whether an order will be delivered late.

    Parameters:
        user_input (dict): Dictionary containing order details.

    Returns:
        prediction, probability
    """
    input_df = pd.DataFrame([user_input])
        # Apply frequency encoding to categorical columns
    for col, mapping in frequency_maps.items():
        input_df[col] = input_df[col].map(mapping)
        input_df[col] = input_df[col].fillna(0)
    # Arrange columns
    input_df = input_df[feature_columns]
        # Make prediction
    print("Input sent to model:")
    print(input_df)
    
    prediction = model.predict(input_df)[0]

    # Get prediction probability
    probability = model.predict_proba(input_df)[0][1]
    if prediction == 1:
        result = "Late Delivery"
    else:
        result = "On-Time Delivery"
    return result, probability