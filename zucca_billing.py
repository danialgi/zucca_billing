import streamlit as st
import pandas as pd
import plotly.express as px
import webbrowser as wb
import openpyxl
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

st.set_page_config(page_title="Zucca Billing", page_icon="🚚", layout="wide")

st.title("🚚 Genuine Inside (M) Sdn. Bhd. - ZUCCA Billing🧾")
st.markdown("##")

st.header("File Upload (1st-15th)")
cart_file1 = st.file_uploader("zucca file 1",type=['xlsx'])
df_cart1 = pd.read_excel(cart_file1)
df_cart1 = df_cart1.drop([0, 1, 2, 3])
df_cart1.columns = df_cart1.iloc[0]
df_cart1 = df_cart1[1:]
df_cart1 = df_cart1.dropna(subset=['Order ID'])
df_cart1.reset_index(inplace=True)
df_cart1 = df_cart1.drop('index', axis=1)
#df_cart1

df_cart1_count=df_cart1.count()
#df_cart1_count
df_cart1_count = df_cart1_count.iloc[0]
#df_cart1_count
#st.write(df_cart1['Total'].sum())
df_cart1_total = pd.DataFrame({
    "Orders": [df_cart1_count],
    "Total": [df_cart1['Total'].sum()]})
#df_cart1_total


st.header("File Upload (16th-31st)")
cart_file2 = st.file_uploader("zucca file 2",type=['xlsx'])
df_cart2 = pd.read_excel(cart_file2)
df_cart2 = df_cart2.drop([0, 1, 2, 3])
df_cart2.columns = df_cart2.iloc[0]
df_cart2 = df_cart2[1:]
df_cart2 = df_cart2.dropna(subset=['Order ID'])
df_cart2.reset_index(inplace=True)
df_cart2 = df_cart2.drop('index', axis=1)
#df_cart2

df_cart2_count=df_cart2.count()
#df_cart2_count
df_cart2_count = df_cart2_count.iloc[0]
#df_cart2_count
#st.write(df_cart2['Total'].sum())
df_cart2_total = pd.DataFrame({
    "Orders": [df_cart2_count],
    "Total": [df_cart2['Total'].sum()]})
#df_cart2_total

df_concat=pd.concat([df_cart1_total, df_cart2_total], axis=0)
#df_concat

#st.write(df_concat['Orders'].sum())
#st.write(df_concat['Total'].sum())
df_total = pd.DataFrame({
    "Orders": [df_concat['Orders'].sum(),"6%"],
    "Total": [df_concat['Total'].sum(),(df_concat['Total'].sum()*6/100)]})

df_final=pd.concat([df_concat, df_total], axis=0)
df_final.reset_index(drop=True,inplace=True)
df_final

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(df_final)

st.download_button(
    label="Download",
    data=csv,
    file_name='ZUCCA Billing.csv',
    mime='text/csv',
)

#st.date_input("Date: ",value="default_value_today")
