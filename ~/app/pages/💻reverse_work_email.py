import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('image2.png')
st.image(image)

st.title("Reverse Work Email Lookup Endpoint")

st.write("Cost: 3 credits / successful request.")
st.write("Resolve LinkedIn Profile from a work email address")

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/profile/resolve/email'

api_key = st.text_input('ENTER YOUR API KEY')
email = st.text_input('ENTER EMAIL ADDRESS')

if st.button('Get Data'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
       'work_email': email,
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

    st.write(response.json())
