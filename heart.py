import numpy as np
import joblib
import streamlit as st

# lode
model=joblib.load("heart_model.pkl")

st.set_page_config(page_title="HEART")

st.title("HEART DISEASE PREDICTION SYSTEM")
st.write("ENTER THE PATIENT'S DETAIL")
Age=st.number_input('Age',min_value=1,step=1)
Sex=st.number_input('Sex',min_value=0,max_value=1)
Chest_pain=st.number_input('Chest pain type',min_value=1)
BP=st.number_input('BP',min_value=0)
Cholesterol=st.number_input('Cholesterol',min_value=0) 
FBS=st.number_input('FBS over 120',min_value=0)
EKG_results=st.number_input('EKG results',min_value=0)
Max_HR=st.number_input( 'Max HR',min_value=0)
Exercise_angina=st.number_input( 'Exercise angina',min_value=0)
ST_depression=st.number_input( 'ST depression',min_value=0.0)
Slope_of_ST=st.number_input( 'Slope of ST',min_value=0)
Number_of_vessels_fluro=st.number_input( 'Number of vessels fluro',min_value=0)
Thallium=st.number_input( 'Thallium',min_value=0) 

if st.button("PREDICTION"):
    input=np.array([[Age,Sex,Chest_pain,BP,Cholesterol, FBS,EKG_results,Max_HR,Exercise_angina,ST_depression,Slope_of_ST,Number_of_vessels_fluro,Thallium]])
    
    prediction = model.predict(input)

if prediction[0]==1:
    st.error("The person is likely to have Heart Disease")
else:st.success("The person is not likely to have Heart Disease")