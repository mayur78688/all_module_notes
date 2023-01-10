import streamlit as st
import pandas as pd
import numpy as np
df=pd.read_csv(r"sunshine.csv")
st.write("""Data set""")
df
st.write("""line chart""")
st.line_chart(df)
st.write("""bar chart""")
st.bar_chart(df)
st.write("""area chart""")
st.area_chart(df)
