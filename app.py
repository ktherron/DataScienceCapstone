import streamlit as st
import pandas as pd
import numpy as np
import pycaret
from pycaret.classification import *

model = load_model('deployment_gb')
       
st.title('Credit Card Fraud Prediction App')
    
# Collect user input
AcountNumber = st.number_input('Customer Account Number', min_value=0, max_value=9999999999) 
CVV = st.number_input('Customer Card CVV', min_value=0, max_value=999)
CustomerAge = st.number_input('Customer Age', min_value=1, max_value=120)
Amount = st.number_input('Amount customer spent', min_value=0, max_value=99999999)
AverageIncomeExpendicture = st.number_input('Customer Average Income Expendicture', min_value=0, max_value=99999999)
Customer_City_Address = st.selectbox('Customers City', ['Abuja', 'Enugu', 'Ibadan', 'Kano', 'Lagos'])
Gender = st.selectbox('Gender', ['male', 'female'])
MaritalStatus = st.selectbox('Marital Status', ['married', 'single', 'unknown', 'divorced'])
CardColour = st.selectbox('Card Color', ['gold', 'white'])
CardType = st.selectbox('Card Type', ['visa', 'verve', 'mastercard'])
Domain = st.selectbox('Domain', ['local', 'international'])

output=""
    
input_dict = {'AcountNumber' : AcountNumber, 'CVV' : CVV, 'CustomerAge' : CustomerAge, 'Gender' : Gender, 
              'MaritalStatus' : MaritalStatus, 'CardColour' : CardColour, 'CardType' : CardType, 'Domain' : Domain,
              'Amount' : Amount, 'AverageIncomeExpendicture' : AverageIncomeExpendicture, 
              'Customer_City_Address' : Customer_City_Address}

input_df = pd.DataFrame([input_dict])
    
if st.button('Predict'):
    output = predict_model(estimator=model, data=input_df)
    output = str(output)
    
    if output[0] == 0:
        st.write("Legitimate Transaction")
    else:
        st.write("Fradulant Transaction")
        
#st.success('Prediction is {}'.format(output))

