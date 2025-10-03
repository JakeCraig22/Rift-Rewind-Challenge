#verifying environment
#running ui shell to plug in data processing

import streamlit as st

st.set_page_config(page_title = "Legends Replayed", page_icon = "🌀", layout="wide")

st.title("Legends Replayed")

st.caption("Turn your match into insights, highlights, and shareable memories!")

name = st.text_input("Summoner name")
if name:
    st.success(f"Welcome **{name}**")

with st.expander("Planned sections"):
    st.markdown("""
    - **Upload match history** (.json/.csv)
- **Stats**: Most played champs, winrate trend, KDA trend
- **AI Recap (Bedrock)**: concise season summary + coaching tips
- **Share Card**: auto-generated PNG for social
    """)



