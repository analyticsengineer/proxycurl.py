import requests
import streamlit as st
from PIL import Image
import re
import json

image = Image.open('proxycurl.png')
st.image(image)

st.title("Employee Search API Endpoint")

st.write("Cost: 10 credits / successful request. + 6 credits / employee returned")
st.write("Search employees of a target by their job title")

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company/employee/search/'

api_key = st.text_input('Enter your api key')
company = st.text_input('Enter company LinkedIn Url')
page_size = st.number_input('Enter page size')
title = st.text_input('Enter the employee title you want to serch for(ceo, software engineer)')

word = re.findall("\D", title)

if st.button('📥'):
    api_key = 'YOUR_API_KEY'
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
       'page_size': page_size,
       'linkedin_company_profile_url': company,
       'keyword_regex': word,
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

    st.write(response.json())
