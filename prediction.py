import pandas as pd
import os
import joblib

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
MODEL_DIR=os.path.join(BASE_DIR,'models')

model=joblib.load(os.path.join(MODEL_DIR,'my_model.pkl'))

data_new = pd.DataFrame({
    'Age Group': ['0-20', '21-40','20-24'],  # example age groups
    'Region Name': ['Europe', 'Asia','Europe'],  # example regions
    'Year': [2025, 2030,2012],
    'Sex': ['Male', 'Female','Male'],
    'cause': ['Injury', 'Communicable','Injury']  # example causes
})

# Convert categorical variables to dummies (same as training)
data_new_encoded = pd.get_dummies(data_new, drop_first=True)

# Make sure all columns match the training data
# Add missing columns with 0
for col in model.feature_names_in_:
    if col not in data_new_encoded.columns:
        data_new_encoded[col] = 0

# Reorder columns to match training
data_new_encoded = data_new_encoded[model.feature_names_in_]

# Predict
predictions = model.predict(data_new_encoded)

# Show predictions
for year, pred in zip(data_new['Year'], predictions):
    print(f"Predicted death rate for {year}: {pred}")

