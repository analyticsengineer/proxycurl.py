import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('image2.png')
st.image(image)

st.title("Personal Email Lookup Endpoint")

st.write("Cost: 0 credit / request.")
st.write("Given an email address, checks if the email address belongs to a disposable email service.")

api_endpoint = 'https://nubela.co/proxycurl/api/disposable-email'

api_key = st.text_input('ENTER YOUR API KEY')
email = st.text_input('ENTER EMAIL ADDRESS')

if st.button('Get Data'):
  header_dic = {'Authorization': 'Bearer ' + api_key}
  params = {
    'email': email,
  }
  response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

    st.write(response.json())
    
   
