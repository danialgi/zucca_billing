import streamlit as st
import pandas as pd
import plotly.express as px
import webbrowser as wb
import openpyxl
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from natsort import natsort_keygen
from io import BytesIO
from datetime import datetime

today_date = datetime.now().strftime('%Y-%m-%d')

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
st.write("UPLOAD SUCCESS")
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

st.markdown("#")
st.header("File Upload (16th-31st)")
cart_file2 = st.file_uploader("zucca file 2",type=['xlsx'])
df_cart2 = pd.read_excel(cart_file2)
df_cart2 = df_cart2.drop([0, 1, 2, 3])
df_cart2.columns = df_cart2.iloc[0]
df_cart2 = df_cart2[1:]
df_cart2 = df_cart2.dropna(subset=['Order ID'])
df_cart2.reset_index(inplace=True)
df_cart2 = df_cart2.drop('index', axis=1)
st.write("UPLOAD SUCCESS")
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

st.write("______________________________________________________________________________________")
#st.write(df_concat['Orders'].sum())
#st.write(df_concat['Total'].sum())
df_total = pd.DataFrame({
    "Orders": [df_concat['Orders'].sum(),"6%"],
    "Total": [df_concat['Total'].sum(),(df_concat['Total'].sum()*6/100)]})

df_final=pd.concat([df_concat, df_total], axis=0)
df_final.reset_index(drop=True,inplace=True)
df_final

# Function to write DataFrames to an Excel file in memory
def dfs_to_excel(df_list, sheet_list):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        for dataframe, sheet in zip(df_list, sheet_list):
            dataframe.to_excel(writer, sheet_name=sheet, index=False)
    output.seek(0)
    return output

df_list = [df_final]
sheet_list = ['Sheet1']

# Convert DataFrames to Excel in memory
excel_file = dfs_to_excel(df_list, sheet_list)

# Streamlit download button
st.download_button(
    label="Download Excel file",
    data=excel_file,
    file_name=f"Zucca_Billing_{today_date}.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
