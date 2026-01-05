# logic_duel.py
import streamlit as st
import pandas as pd
import google.generativeai as genai

# CONFIG
st.set_page_config(page_title="AI Logic Duel", layout="centered")

# API KEY REQUIRED
# Source: https://ai.google.dev
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-pro")

st.title("🧠 AI Logic Duel")

PUZZLE = """
Three people—Alex, Blake, and Casey—are either a Knight (always tells the truth)
or a Knave (always lies).

Alex says: "Blake is a knave."
Blake says: "Casey is a knave."
Casey says: "Alex and Blake are of different types."

Who is the Knight?
"""

st.subheader("Logic Puzzle")
st.write(PUZZLE)

answer = st.text_input("Your answer (e.g., Alex):")

if st.button("Submit"):
    ai_response = model.generate_content(
        f"Solve this logic puzzle and state who is the Knight:\n{PUZZLE}"
    )

    st.subheader("AI Answer")
    st.write(ai_response.text)

    results = pd.DataFrame({
        "Player Answer": [answer],
        "AI Answer": [ai_response.text]
    })

    st.subheader("Round Results")
    st.dataframe(results)
