import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Catalogue", layout="wide")

st.title("📊 Data Catalogue")

uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "xls"])

if uploaded_file:
    try:
        if uploaded_file.name.endswith((".xlsx", ".xls")):
            df = pd.read_excel(uploaded_file)
        else:
            df = pd.read_csv(uploaded_file)

        st.success("File uploaded successfully!")

        st.dataframe(df, use_container_width=True)

        if st.button("Add a new empty row"):
            df.loc[len(df.index)] = [""] * len(df.columns)
            st.dataframe(df, use_container_width=True)

        if st.button("Add a new column"):
            new_col_name = st.text_input("New column name:")
            if new_col_name:
                df[new_col_name] = ""
                st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"Error reading file: {e}")
