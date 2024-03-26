import streamlit as st

st.set_page_config(
    page_title="Crimes in London",
    page_icon=":uk:",
    initial_sidebar_state="expanded",
    layout="centered"
)

st.write("# :oncoming_police_car: Crimes in London")

st.markdown(
    """This project aims to assist those who plan to visit London or those who live in London. With this app, you can walk in the least risky areas to ensure your safety, avoiding places with higher security risks.

The data has been extracted from [https://data.police.uk/about](https://data.police.uk/about), so they are real data.
"""
)
