import numpy as np
import pickle
import streamlit as st

with open('diabetes', 'rb') as f:
    model = pickle.load(f)

# creating function for prediction
def diabetes_prediction(input):
      numpy_array = np.array(input)
      reshaped_input = numpy_array.reshape(1, -1)
      a = model.predict(reshaped_input)
      if (a[0]==0):
          return 'The person is non-diabetic'
      else:
          return 'The person is diabetic'




def main():
    # TITLE
    st.title("DIABETES PREDICTION WEB APP")

    # TAKING INPUT FROM USER
    Pregnancies = st.text_input('NO. OF PREGNANCIES : ')
    Glucose    = st.text_input('GLUCOSE LEVEL : ')
    BloodPressure = st.text_input('BLOOD PRESSURE : ')
    SkinThickness = st.text_input('SKIN THICKNESS : ')
    BMI = st.text_input("B.M.I : ")
    Insulin  = st.text_input('INSULIN LEVEL: ')
    DPC = st.text_input('DiabetesPedigreeFunction : ')
    Age = st.text_input('AGE:')

    diagonosis = ''

    if st.button('Diabetes Test Result'):
          diagonosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, BMI, Insulin, DPC, Age])

          st.success(diagonosis)



if __name__ == '__main__':
    main()




