from predictor import predict_order

sample_order = {
    "Type": "DEBIT",
    "Days for shipment (scheduled)": 1,
    "Sales": 50,
    "Category Name": "Sporting Goods",
    "Department Name": "Fan Shop",
    "Market": "Pacific Asia",
    "Order Country": "India",
    "Order Region": "South Asia",
    "Shipping Mode": "Same Day",
    "Product Price": 50,
    "order_hour": 10,
    "order_month": 1,
    "order_day": 10
}

result, probability = predict_order(sample_order)

print("Prediction:", result)
print("Probability:", probability)