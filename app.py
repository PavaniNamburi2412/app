import streamlit as st
import pandas as pd

# Title of the application
st.title("Data Science Project Application")

# Upload CSV file
file = st.file_uploader("Upload CSV file", type=["csv"])

# Check if file is uploaded
if file is not None:
    # Read data from CSV file
    data = pd.read_csv(file)

    # Display the data
    st.subheader("Data")
    st.write(data)

    # Perform data analysis
    st.subheader("Data Analysis")

    # Example analysis: Show summary statistics
    if st.checkbox("Show Summary Statistics"):
        st.write(data.describe())

    # Example analysis: Show scatter plot
    if st.checkbox("Show Scatter Plot"):
        x_column = st.selectbox("Select X-axis column", data.columns)
        y_column = st.selectbox("Select Y-axis column", data.columns)
        st.write(data.plot.scatter(x=x_column, y=y_column))
