import pickle
import numpy as np
import streamlit as st

pipe = pickle.load(open("pipe.pkl", "rb"))
df = pickle.load(open("df.pkl", "rb"))

# print((df["Company"].unique()))


st.title("Laptop Predictor")

# input details

company = st.selectbox("Brand", df["Company"].unique())
typeName = st.selectbox("Type", df["TypeName"].unique())
ram = st.selectbox("RAM (in GB)", [2, 4, 6, 8, 12, 16, 24, 32, 64])
os = st.selectbox("Operating System", df["OpSys"].unique())
weight = st.number_input("Weight")
touchscreen = st.selectbox("Touchscreen", ["Yes", "No"])
ips = st.selectbox("IPS", ["Yes", "No"])
screen_size = st.number_input("Screen Size")
resolution = st.selectbox("Screen Resolution", ["1920x1080",
                                                "1366x768", "1600x900", "3840x2160", "3200x1800", "2880x1800",
                                                "2560x1600", "2560x1440", "2304x1440"])
cpu = st.selectbox("CPU", df["Cpu brand"].unique())
ssd = st.selectbox("SSD (in GB)", [0, 8, 128, 256, 512, 1024])
hdd = st.selectbox("HDD (in GB)", [0, 128, 256, 500, 512, 1024, 2048])
gpu = st.selectbox("GPU", df["Gpu Brand"].unique())

if st.button("Predict Price"):
    if touchscreen == "Yes":
        touchscreen = 1
    else:
        touchscreen = 0
    if ips == "Yes":
        ips = 1
    else:
        ips = 0
    x_res = int(resolution.split("x")[0])
    y_res = int(resolution.split("x")[1])
    ppi = (((x_res ** 2) + (y_res ** 2)) ** 0.5) / screen_size
    query = np.array([company, typeName, ram, os, weight, touchscreen,
                      ips, ppi, cpu, ssd, hdd, gpu])
    query=query.reshape(1,12)
    st.subheader( "The predicted price of the configuration : " +(str(int(np.exp(pipe.predict(query))[0]))))