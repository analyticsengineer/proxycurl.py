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

api_key = st.text_input('ENTER YOUR API KEY')
job = st.text_input('ENTER LINKEDIN JOB POST URL')


if st.button('Get Data'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
        'url': job,
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

    st.write(response.json())
