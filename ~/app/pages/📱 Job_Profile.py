import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('image2.png')
st.image(image)

st.title("Job Profile Endpoint")

st.write("Cost: 2 credits / successful request.")
st.write("Get structured data of a LinkedIn Job Profile")


api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/job'

api_key = st.text_input('Enter your api key')
job = st.text_input('Enter job post LinkedIn Url')


if st.button('📥'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
        'url': job,
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

    st.write(response.json())
