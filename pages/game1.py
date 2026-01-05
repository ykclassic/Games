# logic_duel_fixed.py
import streamlit as st
import pandas as pd
import google.generativeai as genai
from google.api_core.exceptions import GoogleAPIError

st.set_page_config(page_title="AI Logic Duel", layout="centered")
st.title("🧠 AI Logic Duel")

# ---- API CONFIG ----
if "GEMINI_API_KEY" not in st.secrets:
    st.error("GEMINI_API_KEY not found in Streamlit secrets.")
    st.stop()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# USE SUPPORTED MODEL
model = genai.GenerativeModel("models/gemini-1.5-pro")

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
    try:
        ai_response = model.generate_content(
            PUZZLE,
            request_options={"timeout": 30}
        )

        st.subheader("AI Answer")
        st.write(ai_response.text)

        df = pd.DataFrame({
            "Player Answer": [answer],
            "AI Answer": [ai_response.text]
        })

        st.subheader("Round Results")
        st.dataframe(df)

    except GoogleAPIError as e:
        st.error("Google AI API error occurred.")
        st.code(str(e))
