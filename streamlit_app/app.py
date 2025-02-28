from loguru import logger
import streamlit as st
import requests
import os


api_url = os.environ.get("FASTAPI_PORT")

st.title("Data sender")

choice = ["",""]
selected_data = st.selectbox("Choose a data", choice)

if st.button("Send Color"):
    logger.info(f"sent color: {selected_data}")
    try:
        response = requests.post()
        st.write(response.json())
    except requests.exceptions.RequestException as e:
        logger.info(f"Error sent data: {selected_data}")
        logger.info(f"sending to url : {api_url}")
        st.error(f"Error: {e}")