
import streamlit as st
import pickle

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("House Price Prediction Portal")

# Add input elements for user to provide input for prediction
input_feature1 = st.number_input("Feature 1")
input_feature2 = st.number_input("Feature 2")

# Create a button for prediction
if st.button("Predict"):
    # Prepare the input data as a list
    input_data = [input_feature1, input_feature2]
    
    # Use the loaded model to make predictions
    prediction = model.predict([input_data])

    # Display the prediction
    st.write(f"Predicted Price: {prediction[0]}")
