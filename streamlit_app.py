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
sns.histplot(df[selected_column])
st.pyplot()

st.write("Diagrama de dispersión")
x_axis = st.sidebar.selectbox('Select the x-axis', df.columns)
y_axis = st.sidebar.selectbox('Select the y-axis', df.columns)

fig = px.scatter(df, x=x_axis, y=y_axis)
st.plotly_chart(fig)

st.write("Parcela de pares")
sns.pairplot(df, hue='class')
st.pyplot()
st.write("Description of the data")
st.table(df.describe())

st.header('Matriz de Correlación')

corr = df.corr()
sns.heatmap(corr, annot=True)
st.pyplot()

st.header('Diagrama de caja')

fig = px.box(df, y=selected_column)
st.plotly_chart(fig)

selected_class = st.sidebar.selectbox('Select a class to visualize', df['class'].unique())

if st.sidebar.button('Show Violin Plot'):
    fig = px.violin(df[df['class'] == selected_class], y=selected_column)
    st.plotly_chart(fig)
