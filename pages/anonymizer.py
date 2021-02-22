import streamlit as st
import pandas as pd
from kohokoho import anon

def upload():
    raw_csv = st.file_uploader("Upload Dataset", type=['csv'])
    return raw_csv
    

def write():
    st.title('Upload dataset')
    df = upload()
    if df is not None:
        df = pd.read_csv(df)
        st.subheader('First five rows')
        st.dataframe(df.head())
        st.subheader('Data types of columns')
        st.write(df.dtypes.to_dict())
        koho_df = anon(df)
        st.title('Kohokoho Dataset Anonymizer')

        st.subheader('Select columns with Names')
        name_cols = st.multiselect('Ignore if no such column exist', list(df), key='name_cols')
        if name_cols is not None:
            for col in name_cols:
                koho_df.anon_name(col)
            st.dataframe(koho_df.anon_df().head())

        st.subheader('Select columns with unique Ids')
        id_cols = st.multiselect('Ignore if no such column exist', list(df), key ='id_cols')
        if id_cols is not None:
            for col in id_cols:
                koho_df.anon_id(col)
            st.dataframe(koho_df.anon_df().head())

        st.subheader('Select columns with continuous datatypes')
        continuous_cols = st.multiselect('Ignore if no such column exist', list(df), key ='continuous_cols')
        if continuous_cols is not None:
            for col in continuous_cols:
                koho_df.anon_continuous_num(col)
            st.dataframe(koho_df.anon_df().head())
        
        st.subheader('Select columns with discrete datatypes')
        discrete_cols = st.multiselect('Ignore if no such column exist', list(df), key ='discrete_cols')
        if discrete_cols is not None:
            for col in discrete_cols:
                koho_df.anon_discrete_num(col)
            st.dataframe(koho_df.anon_df().head())
        
        st.subheader('Select columns with categorical datatypes')
        category_cols = st.multiselect('Ignore if no such column exist', list(df), key ='category_cols')
        if category_cols is not None:
            for col in category_cols:
                koho_df.anon_category(col)
            st.dataframe(koho_df.anon_df().head())
        
        st.subheader('Select columns with date datatypes')
        date_cols = st.multiselect('Ignore if no such column exist', list(df), key ='date_cols')
        if date_cols is not None:
            for col in date_cols:
                koho_df.anon_date(col)
            st.dataframe(koho_df.anon_df().head())

        st.subheader('Select columns with email datatypes')
        email_cols = st.multiselect('Ignore if no such column exist', list(df), key ='email_cols')
        if email_cols is not None:
            for col in email_cols:
                koho_df.anon_email(col)
            st.dataframe(koho_df.anon_df().head())
        