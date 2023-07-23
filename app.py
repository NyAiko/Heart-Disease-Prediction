import numpy as np
import pandas as pd
from joblib import load
import streamlit as st
import pysqlite3 as sql


def main():
    lr = load('lr_c.p')
    lr.named_steps.logisticregression.n_jobs = 0
    lr.named_steps.logisticregression.verbose = True
    
    #st.write(lr.get_params())
    st.title("ML Based Heart Disease Prediction")
    st.text("Welcome, I am Dr. NyHeart :) . I make your heart diagnosis as fast as possible.")
    form = st.form(key="form")
    age = form.number_input("Age",step=1,max_value=120)
    cp = form.selectbox("Chest Pain Type: ", ("0. Typical angina","1. atypical angina","2. non-anginal pain","3. asymptomatic"))   
    
    trtbps = form.number_input("Resting Blood Pressure (mmHg)")
    chol = form.number_input("Serum Cholestoral (mg/dl)")
    fbs = form.selectbox("Fasting Blood Sugar > 120 mg/dl",("1. True","0. False"))
    
    restecg = form.selectbox("Resting Electrocardiographic Results: ", ("0. Normal","1. Having ST-T wave abnormality","2. Showing probable or definite left ventricular hypertrophy by Estes' criteria"))

    thalachh = form.number_input("Maximum Heart Rate Achieved: ")
    exng = form.selectbox("Exercise Induced Angina",("1. Yes","0. No"))
    oldpeak = form.number_input("ST Depression Induced by Exercise Relative to Rest")
    slp = form.selectbox("The Slope of the Peak Exercise ST Segment",('0. Upsloping','1. Flat','2. Downsloping'))
    caa = form.selectbox("Number of Major Vessel (0-3) colored by Flourosopy",('0','1','2','3'))
    
    thall=form.selectbox("Thall",('0. Normal','1. Fixed defect','2. Reversible defect'))
    
    col = ['age', 'cp', 'trtbps', 'chol', 'fbs', 'restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa', 'thall']
    var = [age, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]
    input_variable = pd.DataFrame(data=np.array(var).reshape(1,-1),columns=col)
    input_variable = make_input_data(input_variable)
    
    cat_features = ['cp', 'fbs', 'restecg', 'exng', 'slp', 'caa', 'thall']
    input_variable[cat_features]=input_variable[cat_features].astype('category')
    submit_button = form.form_submit_button('Analyse')
    if submit_button:    
        make_predictions(lr,input_variable)
        val = (age, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall)
        save_input_data(val)
        
def make_predictions(model, input_variable):
    prediction = model.predict(input_variable)
    st.header('Diagnosis Results ')
    if int(prediction)==1:
        st.text("The diagnosis result is positive")
        
    else:
        st.text('The diagnosis result is negative')
    return int(prediction)

def make_input_data(input_df):
    cat = ['cp','fbs','restecg','exng','slp','caa','thall']
    for c in cat:
        input_df[c]=input_df[c].apply(split_cat)
    return input_df

def split_cat(x):
    x = str(x)
    return x.split('.')[0]

def save_input_data(val):
    conn = sql.connect('input_data.db')
    cursor = conn.cursor()
    col = ('age', 'cp', 'trtbps', 'chol', 'fbs', 'restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa', 'thall')
    cursor.execute("INSERT INTO INPUT_DATA ('age', 'cp', 'trtbps', 'chol', 'fbs', 'restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa', 'thall') VALUES {}".format(val))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ =='__main__':
    main()

