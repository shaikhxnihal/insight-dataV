import streamlit as st
import pandas as pd

def show_analysis(df):
    st.markdown("### Summary Statistics")
    st.write(df.describe(include='all'))

    st.markdown("### Missing Values")
    st.write(df.isnull().sum())

    st.markdown("### Correlation Matrix")
    corr = df.select_dtypes(include='number').corr()
    st.dataframe(corr)

    st.markdown("### Detect Outliers")
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        st.write(f"{col}: {len(outliers)} outliers")