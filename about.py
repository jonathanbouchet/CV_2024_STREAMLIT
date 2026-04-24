import streamlit as st
import base64
from logger import logger

logger.info("about page")

st.markdown("# About Me")
# st.write(
#     """Customer oriented data scientist with proven ability of delivering valuable insights via data analytics.                    
#     9+ years of professional experience in developing cutting-edge machine learning solutions for insurance leaders"""
# )

st.write("""
I'm a Senior applied AI/ ML engineer with 9+ years of experience, starting in data science and evolving toward building production AI systems. 
My background is machine learning, large scale data processing, and delivering ML solutions grounded in real-world data.
         
In my most recent role, I focused on LLM-powered systems, including multi-agent architectures, RAG pipelines over large datasets, and evaluation frameworks to improve reliability. I’ve worked across the stack—from data ingestion and transformation (Databricks, Spark) to backend services and AI application layers.

I’m particularly interested in problems where AI meets complex, messy data, and where building end-to-end systems matters as much as model performance. I enjoy designing systems that combine data, reasoning, and user interaction.

For my next role, I’m looking to continue working on applied AI—especially LLM or agent-based systems—while staying close to data and maintaining a strong engineering component. Ideally in a team where I can contribute hands-on and help shape systems from early stages through production.


""")

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("assets/picture_2026.png", width=500)

with st.sidebar:
    st.text("You can find me at ")
    col1, col2, col3 = st.sidebar.columns(3)
    with col1:
        st.markdown(
            """<a href="https://www.linkedin.com/in/jonathanbouchet/">
            <img src="data:image/png;base64,{}" width="75">
            </a>""".format(base64.b64encode(open("assets/LI-In-Bug.png", "rb").read()).decode()
            ),
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """<a href="https://www.kaggle.com/jonathanbouchet">
            <img src="data:image/png;base64,{}" width="75">
            </a>""".format(base64.b64encode(open("assets/kaggle.png", "rb").read()).decode()
            ),
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """<a href="https://github.com/jonathanbouchet">
            <img src="data:image/png;base64,{}" width="75">
            </a>""".format(base64.b64encode(open("assets/github.png", "rb").read()).decode()
            ),
            unsafe_allow_html=True,
        )