# data_detective.py
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Data Detective")

st.title("📊 Data Detective")

# Generate hidden pattern
x = np.arange(1, 21)
y = x**2 + np.random.randint(-5, 5, size=len(x))

df = pd.DataFrame({"X": x, "Y": y})

fig = px.scatter(df, x="X", y="Y", title="Find the Pattern")
st.plotly_chart(fig)

guess = st.text_input("What is the relationship between X and Y?")

if st.button("Check"):
    st.write("Underlying pattern: **Quadratic (Y ≈ X²)**")
