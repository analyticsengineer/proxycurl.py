import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('image2.png')
st.image(image)

st.title("Person Lookup Endpoint")

st.write("Cost: 2 credits / successful request.")
st.write("Resolve LinkedIn Profile")

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/profile/resolve'

api_key = st.text_input('ENTER YOUR API KEY')
url = st.text_input('ENTER COMPANY URL')
location = st.text_input('ENTER USER LOCATION')
title = st.text_input('ENTER USER COMPANY TITLE')
last = st.text_input('ENTER USER LAST NAME')
first = st.text_input('ENTER USER FIRST NAME')

if st.button('Get Data'):
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
