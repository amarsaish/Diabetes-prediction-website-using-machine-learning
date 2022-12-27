# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 12:44:41 2022

@author: AMAR
"""

import numpy as np
import pickle
import streamlit as st

#load saved model
loaded_model = pickle.load(open('C:/Users/AMAR/OneDrive/Desktop/projects/diabetes/trained_model.sav','rb'))

#creating a function for prediction

def diabetes_prediction(input_data):
   

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    
  
    
def main():
     
     #giving title for web app
     st.title('diabetes prediction web app')
     
     #getting input data from users
     #Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age
     
     Pregnancies = st.text_input('Number of pregnancies')
     Glucose = st.text_input('Glucose level')
     BloodPressure = st.text_input('blood pressure value')
     SkinThickness = st.text_input('skin thickness value')
     Insulin = st.text_input('insulin level')
     BMI = st.text_input('BMI value')
     DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
     Age = st.text_input('Age of person')
     
     
     #code for prediction
     diagnosis=''
     
     #creating a button for prediction
     if st.button('diabetes test result'):
         diagnosis= diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
         
     st.success(diagnosis)
     
     
     
if __name__ == '__main__':
    main()
     
     
     
     
     
     
     
     