import streamlit as st
from db_scrap.main import *


st.set_page_config(
    page_title="Disney Text Mining",
    page_icon="👋",
)
st.title("Hello")
st.markdown('Page principale')
st.sidebar.markdown('Page principale')

if st.button('Say hello'):
    load_db()