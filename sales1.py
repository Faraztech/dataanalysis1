import streamlit as st
import pandas as pd
import pydeck as pdk
import streamlit_pandas as sp
import os
import re

st.set_page_config(layout="wide")
st.title("Sales Data Analysis")
st.header('By Faraz Younus | M.S. Stats & Data Science', divider='gray')
st.markdown("### Use the Sidebar to Filter Data")    


import os
import streamlit as st
import pandas as pd
import streamlit_pandas as sp

@st.cache
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

files = os.listdir()  
selected_file = st.selectbox("Select a file", files)

df1 = load_data(selected_file)  



create_data = {"Order ID": "text",
                "Product": "multiselect",
                "Purchase Address": "text",
               "Quantity Ordered": "text",
               }

all_widgets = sp.create_widgets(df, create_data)

df = sp.filter_df(df1, all_widgets)
st.title("Streamlit AutoPandas")
st.header("Original DataFrame")
st.write(df1)

st.header("Result DataFrame")
st.write(df)

