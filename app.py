import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model
       
st.set_page_config(page_title = 'Credit Card Fraud Prediction App')

def get_model():
    return load_model('deployment_gb')

def predict(model, data):
    prediction=predict_model(model, data=input_df)
    return prediction['prediction_label'][0]

model = get_model()

st.title('Credit Card Fraud Prediction App')
    
# Collect user input
form = st.form('Outcome')
AcountNumber = form.number_input('Customer Account Number', min_value=0, max_value=9999999999) 
CVV = form.number_input('Customer Card CVV', min_value=0, max_value=999)
CustomerAge = form.number_input('Customer Age', min_value=1, max_value=120)
Amount = form.number_input('Amount customer spent', min_value=0, max_value=99999999)
AverageIncomeExpendicture = form.number_input('Customer Average Income Expendicture', min_value=0, max_value=99999999)
Customer_City_Address = form.selectbox('Customers City', ['Abuja', 'Enugu', 'Ibadan', 'Kano', 'Lagos'])
Gender = form.selectbox('Gender', ['male', 'female'])
MaritalStatus = form.selectbox('Marital Status', ['married', 'single', 'unknown', 'divorced'])
CardColour = form.selectbox('Card Color', ['gold', 'white'])
CardType = form.selectbox('Card Type', ['visa', 'verve', 'mastercard'])
Domain = form.selectbox('Domain', ['local', 'international'])

predict_button = form.form_submit_button('Predict')

input_dict = {'AcountNumber' : AcountNumber, 'CVV' : CVV, 'CustomerAge' : CustomerAge, 'Gender' : Gender, 
              'MaritalStatus' : MaritalStatus, 'CardColour' : CardColour, 'CardType' : CardType, 'Domain' : Domain,
              'Amount' : Amount, 'AverageIncomeExpendicture' : AverageIncomeExpendicture, 
              'Customer_City_Address' : Customer_City_Address}

input_df = pd.DataFrame([input_dict])

    
if predict_button:
    output = predict(model, input_df)
    
    if output == 0:
        st.write("Legitimate Transaction")
    else:
        st.write("Fradulant Transaction")