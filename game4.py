# truth_or_bluff.py
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-pro")

st.title("🤖 Truth or Bluff")

prompt = "Give a surprising but verifiable scientific fact."
fact = model.generate_content(prompt).text

st.subheader("Statement")
st.write(fact)

choice = st.radio("Is this true?", ["True", "False"])

if st.button("Explain"):
    explanation = model.generate_content(
        f"Explain why this statement is true or false:\n{fact}"
    )
    st.write(explanation.text)
