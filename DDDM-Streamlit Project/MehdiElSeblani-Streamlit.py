import pandas as pd
import numpy as np
import seaborn as sns
import plotly as plt
import plotly.express as px
import streamlit as st

df = pd.read_csv(r'C:\Users\Mahdi\Desktop\DDDM-Streamlit Project\Telco_Churn.csv')
df.head()

st.header('Churn Analysis 2021')
