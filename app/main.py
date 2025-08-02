import streamlit as st

st.set_page_config(page_title="Autopilot CEO", layout="wide")
st.title("🤖 Autopilot CEO")
st.write("Your AI-powered business strategist.")

if st.button("Ask Market Intel Bot"):
    st.write("⏳ Running MarketIntel Agent...")
