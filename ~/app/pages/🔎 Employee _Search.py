import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('proxycurl.png')
st.image(image)

st.title("Employee Search API Endpoint")

st.write("Cost: 10 credits / successful request. + 6 credits / employee returned")
st.write("Search employees of a target by their job title")

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company/employee/search/'

api_key = st.text_input('Enter your api key')
company = st.text_input('Enter company LinkedIn Url')

if st.button('📥'):
    api_key = 'YOUR_API_KEY'
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
       'page_size': '1000',
       'linkedin_company_profile_url': company,
       'keyword_regex': '[Cc][Ee][Oo]',
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

    st.write(response.json())
