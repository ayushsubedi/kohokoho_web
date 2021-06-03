import streamlit as st
import pandas as pd
import base64
from kohokoho import anon
import numpy as np


def upload():
    raw_csv = st.file_uploader("Upload Dataset", type=["csv"])
    return raw_csv


def get_table_download_link(df, text, filename):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f"""
    <a href="data:file/csv;base64,{b64}" download={filename}>
    {text}</a>
    """
    return href


def write():
    st.title("Anonymize your data")
    data = upload()
    df_ = pd.read_csv('static/test_dataset/test_dataset1.csv')
    st.markdown(get_table_download_link(df_, "don't have a csv? download a sample", "sample.csv"), unsafe_allow_html=True)

    if data is not None:
        df = pd.read_csv(data)
        st.subheader("Original dataset")
        st.dataframe(df)
        st.subheader("Data types of columns")
        st.write(df.dtypes.to_dict())
        koho_df = anon(df)
        st.title("Kohokoho Dataset Anonymizer")

        st.subheader("Select columns with Names")
        name_cols = st.multiselect(
            "or, with anything that can be replicated for similar field. Ignore if no such column exist.",
            list(df),
            key="name_cols",
        )
        if len(name_cols) > 0:
            for col in name_cols:
                koho_df.anon_name(col)
            if st.checkbox("Show anonymization", key="checkbox_name_cols"):
                col1, col2 = st.beta_columns(2)
                col1.write("Original data")
                col1.dataframe(koho_df._df()[name_cols])
                col2.write("Anonymized data")
                col2.dataframe(koho_df.anon_df()[name_cols])

        st.subheader("Select columns with unique Ids")
        id_cols = st.multiselect(
            "UUID or numeric id or anything else that was meant to be an identifier. Ignore if no such column exist.",
            list(df),
            key="id_cols",
        )
        if len(id_cols) > 0:
            for col in id_cols:
                koho_df.anon_id(col)
            if st.checkbox("Show anonymization", key="checkbox_id_cols"):
                col1, col2 = st.beta_columns(2)
                col1.write("Original data")
                col1.dataframe(koho_df._df()[id_cols])
                col2.write("Anonymized data")
                col2.dataframe(koho_df.anon_df()[id_cols])

        st.subheader("Select columns with continuous datatypes")
        continuous_cols = st.multiselect(
            "mostly implies columns with double/float/decimals. Ignore if no such column exist.",
            (df.select_dtypes([np.number]).columns),
            key="continuous_cols",
        )
        if len(continuous_cols) > 0:
            for col in continuous_cols:
                koho_df.anon_continuous_num(col)
            if st.checkbox("Show anonymization", key="checkbox_con_cols"):
                col1, col2 = st.beta_columns(2)
                col1.write("Original data")
                col1.dataframe(koho_df._df()[continuous_cols])
                col2.write("Anonymized data")
                col2.dataframe(koho_df.anon_df()[continuous_cols])
        st.subheader("Select columns with discrete datatypes")
        discrete_cols = st.multiselect(
            "mostly implies columns with integers. Ignore if no such column exist.",
            (df.select_dtypes([np.number]).columns),
            key="discrete_cols",
        )
        if len(discrete_cols) > 0:
            for col in discrete_cols:
                koho_df.anon_discrete_num(col)
            if st.checkbox("Show anonymization", key="checkbox_dis_cols"):
                col1, col2 = st.beta_columns(2)
                col1.write("Original data")
                col1.dataframe(koho_df._df()[discrete_cols])
                col2.write("Anonymized data")
                col2.dataframe(koho_df.anon_df()[discrete_cols])
        st.subheader("Select columns with categorical datatypes")
        category_cols = st.multiselect(
            "variable that can take on one of a limited, and usually fixed, number of possible values. Ignore if no such column exist.",
            list(df),
            key="category_cols",
        )
        if len(category_cols) > 0:
            for col in category_cols:
                koho_df.anon_category(col)
            if st.checkbox("Show anonymization", key="checkbox_cate_cols"):
                col1, col2 = st.beta_columns(2)
                col1.write("Original data")
                col1.dataframe(koho_df._df()[category_cols])
                col2.write("Anonymized data")
                col2.dataframe(koho_df.anon_df()[category_cols])
        st.subheader("Select columns with date datatypes")
        date_cols = st.multiselect(
            "for dates. Ignore if no such column exist., or if you want this to be real given everything else is anonymized.",
            list(df),
            key="date_cols",
        )
        if len(date_cols) > 0:
            for col in date_cols:
                koho_df.anon_date(col)
            if st.checkbox("Show anonymization", key="checkbox_date_cols"):
                col1, col2 = st.beta_columns(2)
                col1.write("Original data")
                col1.dataframe(koho_df._df()[date_cols])
                col2.write("Anonymized data")
                col2.dataframe(koho_df.anon_df()[date_cols])
        st.subheader("Select columns with email datatypes")
        email_cols = st.multiselect(
            "you know emails. Ignore if no such column exist.",
            list(df),
            key="email_cols",
        )
        if len(email_cols) > 0:
            for col in email_cols:
                koho_df.anon_email(col)
            if st.checkbox("Show anonymization", key="checkbox_email_cols"):
                col1, col2 = st.beta_columns(2)
                col1.write("Original data")
                col1.dataframe(koho_df._df()[email_cols])
                col2.write("Anonymized data")
                col2.dataframe(koho_df.anon_df()[email_cols])
        st.subheader("Anonymized dataset")
        st.dataframe(koho_df.anon_df())
        st.markdown(get_table_download_link(koho_df.anon_df(), "Download anonymized file", "anonymized.csv"), unsafe_allow_html=True)
