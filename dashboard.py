import streamlit as st
import pandas as pd
import numpy as np

st.title("PCB Test AI Dashboard")

# Create sample data
data = pd.DataFrame({
    "Voltage": np.random.uniform(4.7, 5.3, 50),
    "Current": np.random.uniform(0.1, 0.6, 50),
    "Temperature": np.random.randint(25, 70, 50)
})

st.write("Sample Test Data")
st.dataframe(data)

st.line_chart(data)