import streamlit as st
import requests

st.title("Document Research & Theme Identification Chatbot")

user_input = st.text_input("Ask something about your documents:")

if st.button("Send"):
    if user_input:
        response = requests.post("http://127.0.0.1:5000/chat", json={"message": user_input})
        if response.status_code == 200:
            data = response.json()
            st.write("**Bot:**", data.get('answer', ''))
        else:
            st.write("Error communicating with backend.")
