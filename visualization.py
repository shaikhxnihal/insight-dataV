import streamlit as st
import plotly.express as px

def show_visualizations(df):
    chart_type = st.selectbox("Choose a chart type", ["Bar", "Line", "Scatter", "Pie", "Histogram", "Box", "Time Series"])

    if chart_type in ["Bar", "Line", "Scatter", "Box", "Time Series"]:
        x_col = st.selectbox("X-axis", df.columns)
        y_col = st.selectbox("Y-axis", df.columns)

        if chart_type == "Bar":
            fig = px.bar(df, x=x_col, y=y_col)
        elif chart_type == "Line":
            fig = px.line(df, x=x_col, y=y_col)
        elif chart_type == "Scatter":
            fig = px.scatter(df, x=x_col, y=y_col)
        elif chart_type == "Box":
            fig = px.box(df, x=x_col, y=y_col)
        elif chart_type == "Time Series":
            fig = px.line(df, x=x_col, y=y_col)

        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Pie":
        pie_col = st.selectbox("Column for Pie Chart", df.columns)
        fig = px.pie(df, names=pie_col)
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Histogram":
        hist_col = st.selectbox("Column for Histogram", df.columns)
        fig = px.histogram(df, x=hist_col)
        st.plotly_chart(fig, use_container_width=True)
