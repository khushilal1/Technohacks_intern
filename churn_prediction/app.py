





import streamlit as st
import pandas as pd
import pickle

# Load the Rideg classifiet model from the pickle file
model = pickle.load(open('model.pkl', 'rb'))

data_df=pickle.load(open("data.pkl",'rb'))
# Define the columns for user input

columns=['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
       'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'Contract',
       'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges']

# Create a function to preprocess user input make predictions

def predict_churn(input_data):
    # Preprocess the input data
    input_df = pd.DataFrame([input_data], columns=columns)

    # Make predictions using the loaded model
    prediction = model.predict(input_df)
    # probability = model.predict_proba(input_df)[:, 1]

    return prediction

# Create the Streamlit app


def main():


    st.title("Telecom Churn Prediction")
    st.write("Enter the customer details below to predict churn.")

    gender = st.selectbox("Select Gender", data_df['gender'].unique())
    if gender=="Female":
        gender=0
    else:
        gender=1
    
    

    SeniorCitizen = st.selectbox("Is there a Senior Citizens", data_df["SeniorCitizen"].unique())
    st.write("0: No, 1: Yes")
    
    
     
    

    Partner = st.selectbox("Have You a parter", data_df["Partner"].unique())
    st.write("0: No, 1: Yes")
    if Partner=='Yes':
       Partner=1
    else:
        Partner=0
    

    Dependents = st.selectbox("Are you dependents",data_df['Dependents'].unique())
    st.write("0: No, 1: Yes")
    if Dependents=='Yes':
        Dependents=1
    else:
            Dependents=0
    
    
    

    tenure = st.slider("Tenure (months)", 0, 100, 1)
    
    
    
    phone_service = st.selectbox("Have You Phone Service?", data_df['PhoneService'].unique())
    st.write("0: No, 1: Yes")
    if phone_service=='Yes':
        phone_service=1
    else:
            phone_service=0
    
    
    




    MultipleLines= st.selectbox("MultipleLines", data_df['MultipleLines'].unique())
    st.write("0: No, 1: No phone service,2:Yes")
    if MultipleLines=='Yes':
        MultipleLines=2
    elif MultipleLines=="No":
        MultipleLines=0
    else:
            MultipleLines=1
    
    
    

    

    InternetService= st.selectbox("InternetService",data_df ['InternetService'].unique())
    st.write("0:DSL, 1: Optic,2:No")
    
    if InternetService=='DSL':
        InternetService=0
    elif InternetService=="No":
        InternetService=2
    else:
            InternetService=1
    
    
    
    

    OnlineSecurity= st.selectbox("OnlineSecurity", data_df['OnlineSecurity'].unique())
    st.write("2: Yes, 1: No,0:No internet service")
    if OnlineSecurity=='Yes':
        OnlineSecurity=2
    elif OnlineSecurity=="No":
        OnlineSecurity=1
    else:
            OnlineSecurity=0
    
    

 
    OnlineBackup= st.selectbox("OnlineBackup", data_df['OnlineBackup'].unique())
    st.write("2: Yes, 0: No,1:No internet service")
    if OnlineBackup=='Yes':
        OnlineBackup=2
    elif OnlineBackup=="No":
        OnlineBackup=1
    else:
            OnlineBackup=0
    
    


    DeviceProtection= st.selectbox("DeviceProtection", data_df['DeviceProtection'].unique())
    st.write("0: No, 2: Yes,1:No internet service")
    if DeviceProtection=='Yes':
        DeviceProtection=2
    elif DeviceProtection=="No":
        DeviceProtection=1
    else:
            DeviceProtection=0
    
    
    
    
    
    
    TechSupport= st.selectbox("TechSupport", data_df['TechSupport'].unique())
    st.write("0: No, 2: Yes,1:No internet service")
    if TechSupport=='Yes':
        TechSupport=2
    elif TechSupport=="No":
        TechSupport=0
    else:
            TechSupport=1
    
    
    
 
    
    contract = st.selectbox("Contract", data_df['Contract'].unique())
    st.write("0: Month-to-month, 1: One year, 2: Two year")
    if contract=='Month-to-month':
            contract=0
    elif contract=="One year":
        contract=1
    else:
            contract=2
        




    paperless_billing = st.selectbox("Paperless Billing", data_df['PaperlessBilling'].unique())
    st.write("0: No, 1: Yes")
    if paperless_billing=='Yes':
        paperless_billing=1
    else:
            paperless_billing=0
    
    
    
    
    

    payment_method = st.selectbox("Payment Method", data_df['PaymentMethod'].unique())
    st.write("0: Bank transfer (automatic), 1: Credit card (automatic), 2: Electronic check, 3: Mailed check")
    
    if payment_method=='Bank transfer (automatic)':
            payment_method=0
    elif payment_method==" Credit card (automatic)":
        payment_method=1
            
    elif payment_method=="Electronic check":
        payment_method=2
    else:
        payment_method=3
        


    
    
    monthly_charges = st.number_input("Monthly Charges")
    

    
    if st.button("Predict"):
    




        # Create a dictionary to store the user input
        input_data = {
            'gender':gender,
            "SeniorCitizen":SeniorCitizen,
            'Partner':Partner,
            "Dependents":Dependents,
            'tenure': tenure,
            'PhoneService': phone_service,
            'MultipleLines': MultipleLines,
            'InternetService': InternetService,
            'OnlineSecurity':OnlineSecurity,
            'OnlineBackup':OnlineBackup,
            'DeviceProtection': DeviceProtection,
            'TechSupport':TechSupport,
            'Contract': contract,
            'PaperlessBilling': paperless_billing,
            'PaymentMethod': payment_method,
            'MonthlyCharges': monthly_charges,
        }

        


        # # Predict churn based on user input
        churn_prediction = predict_churn(input_data)

        # churn_prediction=churn_probability[1]


        # Display the prediction
        # st.subheader("Churn Prediction")
        if churn_prediction ==1:
            st.write("The customer is likely to churn.")
        else:
            st.write("The customer is unlikely to churn.")

#     # Display the churn probability
#     st.subheader("Churn Probability")

#     st.write("The probability of churn is:", churn_probability)


# Run the Streamlit app
if __name__ == '__main__':
    main()