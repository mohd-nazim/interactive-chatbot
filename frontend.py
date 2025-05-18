import streamlit as st
import requests
import os

st.title("Document Research & Theme Identification Chatbot")

user_input = st.text_input("Ask something about your documents:")

if st.button("Send"):
    if user_input:
        st.write("Sending request to backend...")  # 👈 Debugging message
        
        # ✅ Set the API URL for deployment
        api_url = os.getenv('BACKEND_URL', 'http://127.0.0.1:5000')
        st.write("API URL being called:", api_url)

        try:
            response = requests.post(f"{api_url}/chat", json={"message": user_input})
            st.write("Response Status Code:", response.status_code)  # 👈 Status code
            st.write("Response Text:", response.text)               # 👈 Full response

            if response.status_code == 200:
                data = response.json()
                st.write("**Bot:**", data.get('answer', ''))
            else:
                st.write("❌ **Error communicating with backend.**")
        except Exception as e:
            st.write("❌ **Exception Occurred:**", str(e))
