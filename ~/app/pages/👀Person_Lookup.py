import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('proxycurl.png')
st.image(image)

st.title("Person Lookup Endpoint")

st.write("Cost: 2 credits / successful request.")
st.write("Resolve LinkedIn Profile")

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/profile/resolve'

api_key = st.text_input('Enter your api key')
url = st.text_input('Enter company Url')
location = st.text_input('Enter LinkedIn user location')
title = st.text_input('Enter user company job title')
last = st.text_input('Enter user last name')
first = st.text_input('Enter user first name')

if st.button('📥'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
      'company_domain': url,
      'location': location,
      'title': title,
      'last_name': last,
      'first_name': first,
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

    st.write(response.json())
