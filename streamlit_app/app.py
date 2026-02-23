import os

import requests
import streamlit as st
from loguru import logger

logger.add("/logs/streamlit.log", rotation="500 MB")
st.title("Fontend")

api_url = os.getenv("API_URL", "http://api:8080")

val = st.text_input("Une valeur")
if st.button("Envoyer"):
    res = requests.post(f"{api_url}/predict", data={"data": val})
    st.json(res.json())
    logger.info(f"Appel API : {val}")