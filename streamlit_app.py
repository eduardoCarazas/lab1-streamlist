import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

import ssl

ssl._create_default_https_context = ssl._create_unverified_context
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Exploratory Data Analysis of the Iris Dataset')
