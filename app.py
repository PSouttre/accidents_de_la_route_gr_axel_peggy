import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


st.title("Visualisation gravité des accidents de la route")

df = pd.read_csv("./df_merge1.csv", delimiter = ',', encoding='utf-8')
st.dataframe(df)