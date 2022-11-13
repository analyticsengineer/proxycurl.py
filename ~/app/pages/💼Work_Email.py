import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('proxycurl.png')
st.image(image)

st.title("Work Email Lookup Endpoint")

st.write("Cost: 3 credits / request.")
st.write("Lookup work email address of a LinkedIn Person Profile.")
st.write("Email addresses returned are verified to not be role-based or catch-all emails."
         "Email addresses returned by our API endpoint come with a 95+% deliverability guarantee")

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/profile/email'

api_key = st.text_input('Enter your api key')
profile = st.text_input('Enter your LinkedIn profile Url')

if st.button('📥'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
      'linkedin_profile_url': profile,
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)
    st.write(response.json())
    
   
