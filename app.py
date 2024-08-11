import streamlit as st
import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt

# Title and subheader
st.title("Data Analysis Dashboard")
st.subheader("Analyze Your Data with Python & Streamlit")

# About section in the sidebar
st.sidebar.header("About this App")
st.sidebar.info("""
This application allows users to upload a CSV file and perform various data analysis tasks, including:
- Previewing the dataset
- Checking data types
- Displaying dataset dimensions
- Visualizing null values with a heatmap
- Identifying and removing duplicated values
- Viewing overall statistics of the dataset
""")

# Upload data set
upload = st.file_uploader("Upload your dataset in CSV format", type="csv")
if upload is not None:
    data = pd.read_csv(upload)

    # Show dataset
    if st.checkbox("Preview Dataset"):
        if st.button("Show Head"):
            st.write(data.head())
        if st.button("Show Tail"):
            st.write(data.tail())

    # Show data types
    if st.checkbox("Data Types"):
        st.text("Data Types in the Dataset")
        st.write(data.dtypes)

    # Show shape of data set
    data_shape = st.radio("What dimension do you want to check?", ('Rows', 'Columns'))
    if data_shape == 'Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    elif data_shape == "Columns":
        st.text("Number of Columns")
        st.write(data.shape[1])

    # Find and display null values
    if data.isnull().values.any():
      if st.checkbox("Show Null Values Heatmap"):
        st.text("Heatmap of Null Values")
        plt.figure(figsize=(10, 6))
        # Convert the boolean mask of null values to integer for better visualization
        plt.imshow(data.isnull(), cmap='viridis', aspect='auto')
        plt.colorbar(label='Missing Value Indicator')
        st.pyplot()
    else:
        
         st.success("Congratulations! No missing values in the dataset.")
 
    # Find duplicated values in the dataset
    if data.duplicated().any():
        st.warning("This dataset contains duplicated values.")
        dup = st.selectbox("Do you want to remove duplicated values?", ('Yes', 'No'))
        if dup == 'Yes':
            data = data.drop_duplicates()
            st.text("Duplicated values have been removed.")
        elif dup == "No":
            st.text("No action taken.")

    # Show overall statistics
    if st.checkbox("Overall Statistics"):
        st.text("Summary Statistics of the Dataset")
        st.write(data.describe(include='all'))

else:
    st.info("Please upload a CSV file.")
