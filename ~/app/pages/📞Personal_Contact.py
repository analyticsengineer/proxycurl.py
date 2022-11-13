import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('proxycurl.png')
st.image(image)

st.title("Personal Contact Number Lookup Endpoint")

st.write("Cost: 1 credit / contact number returned.")
st.write("Given an LinkedIn profile, returns a list of personal contact numbers belonging to this identity.")

api_endpoint = 'https://nubela.co/proxycurl/api/contact-api/personal-contact'

api_key = st.text_input('Enter your api key')
personal = st.text_input('Enter personal LinkedIn page Url')


if st.button('📥'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
       'linkedin_profile_url': personal,
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

    st.write(response.json())
