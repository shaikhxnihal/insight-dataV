# devinsights/app.py
import streamlit as st
from data_processor import load_data, filter_data
from visualization import show_visualizations
from stats_analysis import show_analysis

st.set_page_config(page_title="DevInsights", layout="wide")
st.title("DevInsights - Data Trends & Insights for Developers")

with st.sidebar:
    st.header("Upload Your Data")
    uploaded_file = st.file_uploader("Choose a file (CSV, JSON, Excel)", type=["csv", "json", "xlsx"])

if uploaded_file:
    df = load_data(uploaded_file)
    st.success("Data loaded successfully!")

    st.subheader("Data Overview")
    st.dataframe(df.head())

    cols = st.multiselect("Select columns to display", df.columns.tolist(), default=df.columns.tolist())
    filtered_df = filter_data(df, cols)

    st.subheader("Visualizations")
    show_visualizations(filtered_df)

    st.subheader("Statistical Analysis")
    show_analysis(filtered_df)
else:
    st.info("Please upload a dataset to begin.")
