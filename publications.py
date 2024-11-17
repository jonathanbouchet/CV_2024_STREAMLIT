import streamlit as st

with open("assets/publications.md", "r") as f:
    data = f.read()

st.markdown(f"""{data}""")