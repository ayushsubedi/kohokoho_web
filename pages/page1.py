import streamlit as st
import pandas as pd

def upload():
    raw_csv = st.file_uploader("Upload Dataset", type=['csv'])
    return raw_csv

def write():
    st.title('Kohokoho Dataset Anonymizer')
    df = upload()
    if df is not None:
        df = pd.read_csv(df)
        st.subheader('First five rows')
        st.dataframe(df.head())
        st.subheader('Data types of columns')
        st.write(df.dtypes.to_dict())
        