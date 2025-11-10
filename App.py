import streamlit as st
import pandas as pd
import numpy as np

st.title("🩺 Predictive Analytics for Disease Outbreaks")

st.write("""
This app demonstrates predictive analytics for disease outbreaks.
You can upload your dataset (CSV) and view the analysis live.
""")

# File uploader
uploaded_file = st.file_uploader("📂 Upload a CSV dataset", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Data Preview")
    st.write(df.head())

    st.subheader("🔍 Dataset Summary")
    st.write(df.describe())

    st.subheader("📈 Column-wise Mean")
    st.bar_chart(df.mean(numeric_only=True))
else:
    st.info("👆 Upload a CSV file to begin")
