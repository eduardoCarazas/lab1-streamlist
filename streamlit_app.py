import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

import ssl

ssl._create_default_https_context = ssl._create_unverified_context
st.set_option('deprecation.showPyplotGlobalUse', False)

# Loading dataset 
df = pd.read_csv('https://raw.githubusercontent.com/eduardoCarazas/lab1-streamlist/main/DATASET_GASTOS_PAGO_SERVICIOS_BASICOS_HNAL.csv', sep=";")

st.title('Exploratory Data Analysis of the Iris Dataset')
st.header('This app allows you to explore the Iris dataset and visualize the data using various plots.')

st.subheader("DataSet")
st.dataframe(df)
selected_column = st.sidebar.selectbox('Select a column to visualize', df.columns)

st.write("Histograma")
# sns.histplot(df[selected_column])
# st.pyplot()
