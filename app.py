import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Weather Data Dashboard")

uploaded_file = st.file_uploader("Choose a file", type=['csv'])

if uploaded_file is not None:
    st.write("File uploaded successfully")
    df = pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.write(df.head())
    
    st.subheader("Data Summary")
    st.write(df.describe())
    
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select Columns", columns)
    unique_values = df[selected_columns].unique()
    selected_value = st.selectbox("Select Value", unique_values)
    filtered_data = df[df[selected_columns] == selected_value]   
    st.write(filtered_data)
    
    st.subheader("Data Visualization")
    x_column = st.selectbox("X-axis", columns)
    y_column = st.selectbox("Y-axis", columns)
    
    
    if st.button("Generate Plot"):
        st.line_chart(filtered_data.set_index(x_column)[y_column])
else:
    st.write("Waiting for file to be uploaded")