import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('image2.png')
st.image(image)

st.title("Personal Email Lookup Endpoint")

st.write("Cost: 1 credit / email returned.")
st.write("Given an LinkedIn profile, returns a list of personal"
         "emails belonging to this identity. Emails are verified to be deliverable.")

api_endpoint = 'https://nubela.co/proxycurl/api/contact-api/personal-email'

api_key = st.text_input('Enter your api key')
profile = st.text_input('Enter profile LinkedIn page Url')

if st.button('📥'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
      'email_validation': 'include',
      'linkedin_profile_url': profile,
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

    st.write(response.json())
