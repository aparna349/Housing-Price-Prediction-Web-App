import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

st.markdown("""
    <style>
    .stApp {
        background-color: #800000;
        color: white;
    }

    h1 {
        color: #FFD700;
        text-align: center;
    }

    .stButton>button {
        background-color: #FFD700;
        color: black;
        border-radius: 8px;
    }

    .stNumberInput label {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)
data = pd.read_csv("Housing.csv")

# Fill missing values
data = data.fillna(data.mean(numeric_only=True))

# Features
X = data[['area', 'bedrooms', 'bathrooms']]
y = data['price']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)

st.title("🏡 Housing Price Prediction App")

st.write("Enter property details below:")

area = st.number_input("Area (in sq ft)", min_value=0.0)
bedrooms = st.number_input("Number of Bedrooms", min_value=0)
bathrooms = st.number_input("Number of Bathrooms", min_value=0)

if st.button("Predict Price"):
    input_data = [[area, bedrooms, bathrooms]]
    prediction = model.predict(input_data)[0]

    st.subheader(f"💰 Predicted Price: ₹ {round(prediction, 2)}")

    # Category logic
    if prediction > 8000000:
        st.success("🏠 Expensive Property")
    elif prediction > 4000000:
        st.info("🏡 Mid-Range Property")
    else:
        st.warning("👍 Budget Property")