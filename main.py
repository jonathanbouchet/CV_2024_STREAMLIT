import streamlit as st
import db

st.set_page_config(layout="wide",
                   page_title="Jonathan's webpage", page_icon="✅",
                #    initial_sidebar_state="collapsed",
                   menu_items={
                       'Report a bug': "https://github.com/jonathanbouchet",
                       'Get help':"https://github.com/jonathanbouchet",
                       'About': "Jonathan Bouchet webpage"
    })

if 'db_initialized' not in st.session_state:
      st.session_state["db_initialized"] = False
      db.set_db()
      st.session_state["db_initialized"] = True

about_page = st.Page("about.py", title="About Jonathan", icon="❓" )
resume_page = st.Page("resume.py", title="My Resume", icon="📑")
portfolio_page = st.Page("portfolio.py", title="My Portfolio", icon="🔢")
comment_page = st.Page("submit_comment_page.py", title="Comment", icon="🖊️")
# chatbot_page = st.Page("chatbot.py", title="Ask Me Anything", icon="🤖")

if __name__ == "__main__":
    pg = st.navigation([about_page, resume_page, portfolio_page, comment_page])
    pg.run()