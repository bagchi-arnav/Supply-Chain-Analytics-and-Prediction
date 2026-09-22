import streamlit as st
from predictor import predict_order

st.set_page_config(
    page_title="Late Delivery Predictor",
    page_icon="🚚",
    layout="centered"
)

st.title("🚚 Supply Chain Late Delivery Predictor")
st.write("Enter the order details below and click Predict.")

# User Inputs
order_type = st.selectbox(
    "Type",
    ["DEBIT", "TRANSFER", "PAYMENT", "CASH"]
)

shipping_mode = st.selectbox(
    "Shipping Mode",
    ["Standard Class", "Second Class", "First Class", "Same Day"]
)

market = st.selectbox(
    "Market",
    ["Pacific Asia", "USCA", "Europe", "LATAM", "Africa"]
)

country = st.text_input("Order Country")

region = st.text_input("Order Region")

category = st.text_input("Category Name")

department = st.text_input("Department Name")

sales = st.number_input(
    "Sales",
    min_value=0.0
)

product_price = st.number_input(
    "Product Price",
    min_value=0.0
)

scheduled_days = st.number_input(
    "Scheduled Shipping Days",
    min_value=0
)

order_hour = st.slider(
    "Order Hour",
    0,
    23,
    12
)

order_month = st.slider(
    "Order Month",
    1,
    12,
    1
)

order_day = st.slider(
    "Order Day",
    1,
    31,
    1
)

if st.button("Predict"):

    user_input = {
        "Type": order_type,
        "Days for shipment (scheduled)": scheduled_days,
        "Sales": sales,
        "Category Name": category,
        "Department Name": department,
        "Market": market,
        "Order Country": country,
        "Order Region": region,
        "Shipping Mode": shipping_mode,
        "Product Price": product_price,
        "order_hour": order_hour,
        "order_month": order_month,
        "order_day": order_day
    }

    result, probability = predict_order(user_input)
    st.success(f"Prediction: {result}")
    st.info(f"Probability of Late Delivery: {probability:.2%}")
