import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

import ssl

ssl._create_default_https_context = ssl._create_unverified_context
st.set_option('deprecation.showPyplotGlobalUse', False)

# Loading dataset 
df = pd.read_csv('https://raw.githubusercontent.com/eduardoCarazas/lab1-streamlist/main/DATASET_GASTOS_PAGO_SERVICIOS_BASICOS_HNAL.csv')

st.title('Análisis exploratorio - Delitos Denunciados 2020')

st.subheader("DataSet")
st.dataframe(df)
selected_column = st.sidebar.selectbox('Select a column to visualize', df.columns)

st.write("Histograma")
sns.histplot(df[selected_column])
st.pyplot()

st.write("Diagrama de dispersión")
x_axis = st.sidebar.selectbox('Select the x-axis', df.columns)
y_axis = st.sidebar.selectbox('Select the y-axis', df.columns)

fig = px.scatter(df, x=x_axis, y=y_axis)
st.plotly_chart(fig)

st.header('Matriz de Correlación')

corr = df.corr()
sns.heatmap(corr, annot=True)
st.pyplot()
