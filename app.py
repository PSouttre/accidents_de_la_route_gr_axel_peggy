import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Visualisation gravité des accidents de la route")


df = pd.read_csv("./df_merge1.csv", delimiter=',', encoding='utf-8')


st.dataframe(df) # Afficher les données sous forme de tableau


corr = df.corr() # Matrice de corrélation

plt.figure(figsize=(10,8))  
sns.heatmap(corr, cmap='coolwarm', annot=True, linewidth=0.9)

st.pyplot(plt) # Afficher le graphique dans Streamlit

print(df.dtypes)