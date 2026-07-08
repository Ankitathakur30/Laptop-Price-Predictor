import streamlit as st
import pandas as pd
import numpy as np


import pickle

pipe=pickle.load(open("models/model.pkl","rb"))
df=pickle.load(open("data/df.pkl","rb"))
st.set_page_config(page_title="Laptop Price Predictor",page_icon="💻",layout="centered")
st.title("Laptop Price Predictor💻")
st.markdown("Predict the market price of a laptop using a Machine Learning ensemble model.")

col1,col2=st.columns(2)

with col1:
    company=st.selectbox('Brand',df['Company'].unique())
    type=st.selectbox('Type',df['TypeName'].unique())
    ram=st.selectbox('Ram',[2,4,6,8,12,16,24,32,64])
    weight=st.number_input('Weight of Laptop')
    touchscreen=st.selectbox('Touchscreen',['Yes','No'])
    ips=st.selectbox('IPS',['Yes','No'])

with col2:
    screen_size=st.number_input('Screen Size')
    resolution=st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
    cpu=st.selectbox('CPU',df['Cpu brand'].unique())
    hdd=st.selectbox('HDD(in GB)',[0,128,256,512,1024,2848])
    ssd=st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])
    gpu=st.selectbox('GPU',df['Gpu brand'].unique())
    os=st.selectbox('OS',df['os'].unique())

    st.sidebar.title("About")

    st.sidebar.info(
    """
    This application predicts laptop prices using a Voting Regressor trained on multiple machine learning models.

    Models Used:
    - Random Forest
    - Extra Trees
    - Gradient Boosting
    - XGBoost
    """
    )

if st.button('Predict Price'):
    if touchscreen=='Yes':
        touchscreen=1
    else:
        touchscreen=0

    if ips=='Yes':
        ips=1
    else:
        ips=0

    X_res=float(resolution.split('x')[0])
    Y_res=float(resolution.split('x')[1])
    ppi=((X_res**2)+(Y_res**2))**0.5/screen_size
    query=pd.DataFrame([[company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os]],columns=['Company','TypeName','Ram','Weight','Touchscreen','IPS','PPI','Cpu brand','HDD','SSD','Gpu brand','os'])
    with st.spinner("Predicting..."):
        prediction=pipe.predict(query)
    st.success(f"Estimated Price: ₹ {round(np.exp(prediction[0]))}")
    st.balloons()
    st.metric(
    label="Estimated Laptop Price",
    value=f"₹ {round(np.exp(prediction[0]))}"
    )